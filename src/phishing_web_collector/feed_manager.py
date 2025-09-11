import asyncio
import json
import logging
from collections import defaultdict
from typing import Callable, Dict, Iterable, List, Optional, Type

from phishing_web_collector.feeds.feed import AbstractFeed
from phishing_web_collector.feeds.sources import (
    AdGuardHomeFeed,
    BinaryDefenceIpFeed,
    BlockListDeIpFeed,
    BotvrijFeed,
    C2IntelFeed,
    C2TrackerIpFeed,
    CertPLFeed,
    DangerousDomainsFeed,
    GreenSnowIpFeed,
    MalwareWorldFeed,
    MiraiSecurityIpFeed,
    OpenPhishFeed,
    PhishingArmyFeed,
    PhishingDatabaseFeed,
    PhishStatsApiFeed,
    PhishTankFeed,
    ProofPointIpFeed,
    ThreatViewFeed,
    TweetFeed,
    UrlAbuseFeed,
    UrlHausFeed,
    ValdinFeed,
)
from phishing_web_collector.models import FeedSource, PhishingEntry
from phishing_web_collector.utils import load_json, remove_none_from_dict

logger = logging.getLogger(__name__)

# Mapping of feed sources to their corresponding classes
SOURCES_MAP: Dict[FeedSource, Type[AbstractFeed]] = {
    FeedSource.AD_GUARD_HOME: AdGuardHomeFeed,
    FeedSource.BINARY_DEFENCE_IP: BinaryDefenceIpFeed,
    FeedSource.BLOCKLIST_DE_IP: BlockListDeIpFeed,
    FeedSource.BOTVRIJ: BotvrijFeed,
    FeedSource.C2_INTEL_DOMAIN: C2IntelFeed,
    FeedSource.C2_TRACKER_IP: C2TrackerIpFeed,
    FeedSource.CERT_PL: CertPLFeed,
    FeedSource.DANGEROUS_DOMAINS: DangerousDomainsFeed,
    FeedSource.GREEN_SNOW_IP: GreenSnowIpFeed,
    FeedSource.MALWARE_WORLD: MalwareWorldFeed,
    FeedSource.MIRAI_SECURITY_IP: MiraiSecurityIpFeed,
    FeedSource.OPEN_PHISH: OpenPhishFeed,
    FeedSource.PHISHING_ARMY: PhishingArmyFeed,
    FeedSource.PHISHING_DATABASE: PhishingDatabaseFeed,
    # FeedSource.PHISH_STATS: PhishStatsFeed,
    FeedSource.PHISH_STATS: PhishStatsApiFeed,
    FeedSource.PHISH_TANK: PhishTankFeed,
    FeedSource.PROOF_POINT_IP: ProofPointIpFeed,
    FeedSource.THREAT_VIEW_DOMAIN: ThreatViewFeed,
    FeedSource.TWEET_FEED: TweetFeed,
    FeedSource.URL_ABUSE: UrlAbuseFeed,
    FeedSource.URL_HAUS: UrlHausFeed,
    FeedSource.VALDIN: ValdinFeed,
}

EntryFilter = Callable[["PhishingEntry"], bool]


class FeedManager:

    def __init__(
        self,
        sources: List[FeedSource],
        storage_path: str,
        filters: Optional[Iterable[EntryFilter]] = None,
    ):
        self.providers = [SOURCES_MAP[source](storage_path) for source in sources]
        self.entries: List[PhishingEntry] = []

        self._global_filters: List[EntryFilter] = list(filters) if filters else []
        self._per_feed_filters: Dict[FeedSource, List[EntryFilter]] = {}

    @property
    def entry_map(self) -> Dict[str, List[PhishingEntry]]:
        """Return a cached dictionary of phishing entries with the URL as the key, refreshing if entries have changed."""
        if not hasattr(self, "_entry_map_cache") or self._entries_changed():
            data = defaultdict(list)
            for entry in self.entries:
                data[entry.url].append(
                    {
                        "targeted_url": entry.targeted_url,
                        "reference_url": entry.reference_url,
                        "source": entry.source.value,
                        "fetch_date": entry.fetch_date.isoformat(),
                    }
                )
            self._entry_map_cache = dict(data)
            self._entries_hash = hash(tuple(self.entries))

        return self._entry_map_cache

    def _entries_changed(self):
        """Check if the entries list has changed since the last cache."""
        return (
            not hasattr(self, "_entries_hash")
            or hash(tuple(self.entries)) != self._entries_hash
        )

    def export_to_json(self, filename: str = "phishing_data.json"):
        """Export all phishing data to a single JSON file, with the phishing URL as the key."""
        with open(filename, "w") as f:
            json.dump(remove_none_from_dict(self.entry_map), f, indent=4)

        logger.info(f"Exported phishing data to {filename}")

    def load_from_json(self, filename: str = "phishing_data.json"):
        """Import phishing data from a single JSON file, with the phishing URL as the key"""
        try:
            data = load_json(filename)

            entries = []
            for url, records in data.items():
                for record in records:
                    entry = PhishingEntry(
                        url=url,
                        targeted_url=record["targeted_url"],
                        reference_url=record["reference_url"],
                        source=FeedSource(record["source"]),
                        fetch_date=record["fetch_date"],
                    )
                    entries.append(entry)
            self.entries = entries
            logger.info(f"Imported phishing data from {filename}")

        except Exception as e:  # noqa
            logger.error(f"Failed to import phishing data from {filename}: {e}")

    def find_entry(self, domain: str) -> Optional[List[PhishingEntry]]:
        return self.entry_map[domain]

        # --- ASYNC ---

    async def refresh_all(self, force: bool = False):
        """Asynchronously refresh all feeds."""
        await asyncio.gather(*(p.refresh(force) for p in self.providers))

    async def retrieve_all(self) -> List["PhishingEntry"]:
        """Asynchronously retrieve entries from all feeds."""
        coros = [provider.retrieve() for provider in self.providers]
        results = await asyncio.gather(*coros)
        self.entries = self._postprocess(results)
        return self.entries

    # --- SYNC ---

    def sync_refresh_all(self, force: bool = False):
        """Refresh synchronously all feeds."""
        for provider in self.providers:
            provider.refresh_sync(force)

    def sync_retrieve_all(self) -> List["PhishingEntry"]:
        """Retrieve synchronously  entries from all feeds."""
        all_entries = []
        for provider in self.providers:
            entries = provider.retrieve_sync()
            all_entries.extend(entries)
        self.entries = self._postprocess(all_entries)
        return self.entries

    def add_filter(self, f: EntryFilter) -> None:
        """Add a global filter that applies to all feeds."""
        self._global_filters.append(f)

    def add_filter_for_feed(self, feed_source: FeedSource, f: EntryFilter) -> None:
        """Add a filter that applies only to a specific feed."""
        self._per_feed_filters.setdefault(feed_source, []).append(f)

    def clear_filters(self) -> None:
        """Clear all filters."""
        self._global_filters.clear()
        self._per_feed_filters.clear()

    def _accept(self, entry: PhishingEntry) -> bool:
        for f in self._global_filters:
            if not f(entry):
                return False
        for f in self._per_feed_filters.get(entry.source, []):
            if not f(entry):
                return False
        return True

    def _postprocess(self, results: List[PhishingEntry]) -> List[PhishingEntry]:
        seen: set = set()
        out: List["PhishingEntry"] = []
        print(results)
        for entry in results:
            if not self._accept(entry):
                continue
            if entry in seen:
                continue
            seen.add(entry)
            out.append(entry)

        return out

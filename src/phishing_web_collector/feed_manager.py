import asyncio
import json
import logging
from collections import defaultdict
from typing import Dict, List, Optional, Type

from phishing_web_collector.feeds.feed import AbstractFeed
from phishing_web_collector.feeds.sources import (
    BinaryDefenceIpFeed,
    BlockListDeIpFeed,
    BotvrijFeed,
    C2IntelFeed,
    C2TrackerIpFeed,
    CertPLFeed,
    GreenSnowIpFeed,
    MiraiSecurityIpFeed,
    OpenPhishFeed,
    PhishingArmyFeed,
    PhishingDatabaseFeed,
    PhishStatsApiFeed,
    PhishStatsFeed,
    PhishTankFeed,
    ProofPointIpFeed,
    ThreatViewFeed,
    TweetFeed,
    UrlAbuseFeed,
    UrlHausFeed,
    ValdinFeed,
)
from phishing_web_collector.models import FeedSource, PhishingEntry
from phishing_web_collector.utils import remove_none_from_dict

logger = logging.getLogger(__name__)

SOURCES_MAP: Dict[FeedSource, Type[AbstractFeed]] = {
    FeedSource.BINARY_DEFENCE_IP: BinaryDefenceIpFeed,
    FeedSource.BLOCKLIST_DE_IP: BlockListDeIpFeed,
    FeedSource.BOTVRIJ: BotvrijFeed,
    FeedSource.C2_INTEL_DOMAIN: C2IntelFeed,
    FeedSource.C2_TRACKER_IP: C2TrackerIpFeed,
    FeedSource.CERT_PL: CertPLFeed,
    FeedSource.GREEN_SNOW_IP: GreenSnowIpFeed,
    FeedSource.MIRAI_SECURITY_IP: MiraiSecurityIpFeed,
    FeedSource.OPEN_PHISH: OpenPhishFeed,
    FeedSource.PHISHING_ARMY: PhishingArmyFeed,
    FeedSource.PHISHING_DATABASE: PhishingDatabaseFeed,
    FeedSource.PHISH_STATS: PhishStatsFeed,
    FeedSource.PHISH_STATS_API: PhishStatsApiFeed,
    FeedSource.PHISH_TANK: PhishTankFeed,
    FeedSource.PROOF_POINT_IP: ProofPointIpFeed,
    FeedSource.THREAT_VIEW_DOMAIN: ThreatViewFeed,
    FeedSource.TWEET_FEED: TweetFeed,
    FeedSource.URL_ABUSE: UrlAbuseFeed,
    FeedSource.URL_HAUS: UrlHausFeed,
    FeedSource.VALDIN: ValdinFeed,
}


class FeedManager:

    def __init__(self, sources: List[FeedSource], storage_path: str):
        self.providers = [SOURCES_MAP[source](storage_path) for source in sources]
        self.entries: List[PhishingEntry] = []

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

    async def refresh_all(self, force: bool = False):
        """Refresh all configured feeds_data asynchronously."""
        await asyncio.gather(*(provider.refresh(force) for provider in self.providers))

    def sync_refresh_all(self, force: bool = False):
        """Refresh all configured feeds_data synchronously"""
        asyncio.run(self.refresh_all(force))

    async def retrieve_all(self) -> List[PhishingEntry]:
        """Retrieve all phishing entries from all feeds_data asynchronously."""
        results = await asyncio.gather(
            *(asyncio.to_thread(provider.retrieve) for provider in self.providers)
        )
        self.entries = [entry for result in results for entry in result]
        return self.entries

    def sync_retrieve_all(self) -> List[PhishingEntry]:
        """Retrieve all phishing entries from all feeds_data synchronously."""
        return asyncio.run(self.retrieve_all())

    def export_to_json(self, filename: str = "phishing_data.json"):
        """Export all phishing data to a single JSON file, with the phishing URL as the key."""
        with open(filename, "w") as f:
            json.dump(remove_none_from_dict(self.entry_map), f, indent=4)

        logger.info(f"Exported phishing data to {filename}")

    def load_from_json(self, filename: str = "phishing_data.json"):
        """Import phishing data from a single JSON file, with the phishing URL as the key"""
        try:
            with open(filename, "r") as f:
                data = json.load(f)

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

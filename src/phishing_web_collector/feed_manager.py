import asyncio
import json
import logging
from collections import defaultdict
from typing import Dict, List, Type

from phishing_web_collector.feeds.feed import AbstractFeed
from phishing_web_collector.feeds.sources import BotvrijFeed, C2IntelFeed, \
    CertPLFeed, OpenPhishFeed, PhishTankFeed, PhishingArmyFeed, \
    PhishingDatabaseFeed, ThreatViewFeed, TweetFeed, UrlAbuseFeed, \
    ValdinFeed

from phishing_web_collector.models import FeedSource, PhishingEntry

logger = logging.getLogger(__name__)

SOURCES_MAP: Dict[FeedSource, Type[AbstractFeed]] = {
    FeedSource.PHISH_TANK: PhishTankFeed,
    FeedSource.OPEN_PHISH: OpenPhishFeed,
    FeedSource.TWEET_FEED: TweetFeed,
    FeedSource.PHISHING_ARMY: PhishingArmyFeed,
    FeedSource.CERT_PL: CertPLFeed,
    FeedSource.THREAT_VIEW_DOMAIN: ThreatViewFeed,
    FeedSource.C2_INTEL_DOMAIN: C2IntelFeed,
    FeedSource.BOTVRIJ: BotvrijFeed,
    FeedSource.URL_ABUSE: UrlAbuseFeed,
    FeedSource.VALDIN: ValdinFeed,
    FeedSource.PHISHING_DATABASE: PhishingDatabaseFeed,
}


class FeedManager:

    def __init__(self, sources: List[FeedSource], storage_path: str):
        self.providers = [SOURCES_MAP[source](storage_path) for source in
                          sources]
        self.entries = []

    async def refresh_all(self, force: bool = False):
        """Refresh all configured feeds_data asynchronously"""
        await asyncio.gather(
            *(provider.refresh(force) for provider in self.providers))

    def sync_refresh_all(self, force: bool = False):
        """Refresh all configured feeds_data synchronously"""
        asyncio.run(self.refresh_all(force))

    async def retrieve_all(self) -> List[PhishingEntry]:
        """Retrieve all phishing entries from all feeds_data asynchronously"""
        results = await asyncio.gather(
            *(asyncio.to_thread(provider.retrieve) for provider in
              self.providers)
        )
        self.entries = [entry for result in results for entry in result]
        return self.entries

    def sync_retrieve_all(self) -> List[PhishingEntry]:
        """Retrieve all phishing entries from all feeds_data synchronously"""
        return asyncio.run(self.retrieve_all())

    async def export_to_json(self, filename: str = "phishing_data.json"):
        """Export all phishing data to a single JSON file, with the phishing URL as the key"""
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

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        logger.info(f"Exported phishing data to {filename}")

    def sync_export_to_json(self, filename: str = "phishing_data.json"):
        """Export synchronously all phishing data to a single JSON file, with the phishing URL as the key"""
        asyncio.run(self.export_to_json(filename))

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
                        fetch_date=record["fetch_date"]
                    )
                    entries.append(entry)
            self.entries = entries
            logger.info(f"Imported phishing data from {filename}")
        except Exception as e:
            logger.error(
                f"Failed to import phishing data from {filename}: {e}")

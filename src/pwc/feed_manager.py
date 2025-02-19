import asyncio
import json
import logging
from collections import defaultdict
from typing import Dict, List, Type

from pwc.feeds.feed import AbstractFeed
from pwc.feeds.sources.botvrij_feed import BotvrijFeed
from pwc.feeds.sources.c2_intel_feed import C2IntelFeed
from pwc.feeds.sources.cert_pl_feed import CertPLFeed
from pwc.feeds.sources.open_phish_feed import OpenPhishFeed
from pwc.feeds.sources.phish_tank_feed import PhishTankFeed
from pwc.feeds.sources.phishing_army_feed import PhishingArmyFeed
from pwc.feeds.sources.phishing_database_feed import PhishingDatabaseFeed
from pwc.feeds.sources.threat_view_feed import ThreatViewFeed
from pwc.feeds.sources.tweet_feed_feed import TweetFeedProvider
from pwc.feeds.sources.url_abuse_feed import UrlAbuseFeed
from pwc.feeds.sources.valdin_feed import ValdinFeed
from pwc.models import FeedSource, PhishingEntry

logger = logging.getLogger(__name__)


class FeedManager:
    sources_map: Dict[FeedSource, Type[AbstractFeed]] = {
        FeedSource.PHISH_TANK: PhishTankFeed,
        FeedSource.OPEN_PHISH: OpenPhishFeed,
        FeedSource.TWEET_FEED: TweetFeedProvider,
        FeedSource.PHISHING_ARMY: PhishingArmyFeed,
        FeedSource.CERT_PL: CertPLFeed,
        FeedSource.THREAT_VIEW_DOMAIN: ThreatViewFeed,
        FeedSource.C2_INTEL_DOMAIN: C2IntelFeed,
        FeedSource.BOTVRIJ: BotvrijFeed,
        FeedSource.URL_ABUSE: UrlAbuseFeed,
        FeedSource.VALDIN: ValdinFeed,
        FeedSource.PHISHING_DATABASE: PhishingDatabaseFeed,
    }

    def __init__(self, sources: List[FeedSource], storage_path: str):
        self.providers = [self.sources_map[source](storage_path) for source in sources]

    async def refresh_all(self, force: bool = False):
        """Refresh all configured feeds_data asynchronously"""
        await asyncio.gather(*(provider.refresh(force) for provider in self.providers))

    def sync_refresh_all(self, force: bool = False):
        """Refresh all configured feeds_data synchronously"""
        asyncio.run(self.refresh_all(force))

    async def retrieve_all(self) -> List[PhishingEntry]:
        """Retrieve all phishing entries from all feeds_data asynchronously"""
        results = await asyncio.gather(
            *(asyncio.to_thread(provider.retrieve) for provider in self.providers)
        )
        entries = [entry for result in results for entry in result]  # Flatten list
        return entries

    def sync_retrieve_all(self) -> List[PhishingEntry]:
        """Retrieve all phishing entries from all feeds_data synchronously"""
        return asyncio.run(self.retrieve_all())

    async def export_to_json(self, filename: str = "phishing_data.json"):
        """Export all phishing data to a single JSON file, with the phishing URL as the key"""
        entries = await self.retrieve_all()
        data = defaultdict(list)

        for entry in entries:
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

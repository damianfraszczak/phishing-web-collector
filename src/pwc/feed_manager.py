import asyncio
import json
import logging
from collections import defaultdict
from typing import List, Dict, Type

from feeds.feed import AbstractFeed
from models import FeedSource, PhishingEntry

logger = logging.getLogger(__name__)

class FeedManager:
    provider_map: Dict[FeedSource, Type[AbstractFeed]] = {

    }

    def __init__(self, sources: List[FeedSource], storage_path: str):
        self.providers = [self.provider_map[source](storage_path) for source in sources]

    async def refresh_all(self, force: bool = False):
        """Refreshes all configured feeds_data asynchronously"""
        await asyncio.gather(*(provider.refresh(force) for provider in self.providers))

    def sync_refresh_all(self, force: bool = False):
        """Synchronous wrapper for refresh_all"""
        asyncio.run(self.refresh_all(force))

    async def retrieve_all(self) -> List[PhishingEntry]:
        """Retrieves all phishing entries from all feeds_data asynchronously"""
        results = await asyncio.gather(*(asyncio.to_thread(provider.retrieve) for provider in self.providers))
        entries = [entry for result in results for entry in result]  # Flatten list
        return entries

    def sync_retrieve_all(self) -> List[PhishingEntry]:
        """Synchronous wrapper for retrieve_all"""
        return asyncio.run(self.retrieve_all())

    async def export_to_json(self, filename: str = "phishing_data.json"):
        """Exports all phishing data to a single JSON file, with the phishing URL as the key"""
        entries = await self.retrieve_all()
        data = defaultdict(list)

        for entry in entries:
            data[entry.url].append({
                "targeted_url": entry.targeted_url,
                "reference_url": entry.reference_url,
                "source": entry.source.value,
                "fetch_date": entry.fetch_date.isoformat()
            })

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        logger.info(f"Exported phishing data to {filename}")

    def sync_export_to_json(self, filename: str = "phishing_data.json"):
        """Synchronous wrapper for export_to_json"""
        asyncio.run(self.export_to_json(filename))

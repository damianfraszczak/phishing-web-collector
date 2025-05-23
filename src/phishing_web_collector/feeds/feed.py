import asyncio
import logging
import time
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import List

from phishing_web_collector.models import FeedSource, PhishingEntry
from phishing_web_collector.taxonomies import RefreshInterval

logger = logging.getLogger(__name__)


class AbstractFeed(ABC):
    FEED_TYPE: FeedSource
    INTERVAL: int = RefreshInterval.DAILY.value
    FILE_EXTENSION: str = "txt"

    def __init__(self, storage_path: str):
        self.storage_path = Path(storage_path) / self.FEED_TYPE.value
        self.storage_path.mkdir(exist_ok=True, parents=True)

    def get_feed_path(self) -> Path:
        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H")
        return (
            self.storage_path
            / f"{self.FEED_TYPE.value}_{timestamp}.{self.FILE_EXTENSION}"
        )

    def should_refresh(self) -> bool:
        feed_path = self.get_feed_path()

        if not feed_path.exists():
            return True

        file_mtime = feed_path.stat().st_mtime  #
        now = time.time()
        interval_sec = self.INTERVAL / 1000

        return (now - file_mtime) > interval_sec

    async def refresh(self, force: bool = False) -> None:
        if force or self.should_refresh():
            logger.info(f"Refreshing feed: {self.FEED_TYPE.value}")
            raw_data = await self.fetch_feed()
            if raw_data:
                feed_path = self.get_feed_path()
                feed_path.write_text(raw_data, encoding="utf-8")
                logger.info(f"Feed saved: {feed_path}")
            else:
                logger.warning(
                    f"Skipping save - No data fetched for {self.FEED_TYPE.value}"
                )
        else:
            logger.info(f"Skipping refresh, feed is up to date: {self.FEED_TYPE.value}")

    def retrieve(self) -> List[PhishingEntry]:
        asyncio.run(self.refresh())
        all_files = sorted(self.storage_path.iterdir(), key=lambda f: f.stat().st_mtime)
        if not all_files:
            logger.warning(f"No data found for feed: {self.FEED_TYPE.value}")
            return []

        logger.info(f"Feed range: {all_files[0].name} -> {all_files[-1].name}")

        unique_entries = set()

        for file in all_files:
            entries = self.parse_feed(file.read_text(encoding="utf-8"))
            unique_entries.update(entries)

        return list(unique_entries)

    @abstractmethod
    def parse_feed(self, raw_data: str) -> List[PhishingEntry]:
        pass

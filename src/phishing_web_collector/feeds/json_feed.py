import json
import logging
from abc import abstractmethod
from datetime import datetime
from typing import Dict, List, Optional

from phishing_web_collector.feeds.file_based_feed import FileBasedFeed
from phishing_web_collector.models import PhishingEntry

logger = logging.getLogger(__name__)


class JSONFeed(FileBasedFeed):
    FILE_EXTENSION = "json"

    def parse_feed(self, raw_data: str) -> List[PhishingEntry]:
        try:
            data = json.loads(raw_data)
            fetch_time = datetime.utcnow()
            return [
                entry for item in data if (entry := self.parse_entry(item, fetch_time))
            ]
        except json.JSONDecodeError:
            logger.error(f"Failed to parse JSON for {self.FEED_TYPE.value}")
            return []

    @abstractmethod
    def parse_entry(self, item: Dict, fetch_time: datetime) -> Optional[PhishingEntry]:
        pass

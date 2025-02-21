from datetime import datetime
from typing import List, Optional

from phishing_web_collector.feeds.file_based_feed import FileBasedFeed
from phishing_web_collector.models import PhishingEntry


class URLListFeedProvider(FileBasedFeed):
    def parse_feed(self, raw_data: str) -> List[PhishingEntry]:
        fetch_time = datetime.utcnow()
        entries = [
            entry
            for line in raw_data.splitlines()
            if not line.startswith("#")
            if (entry := self.parse_line(line.strip(), fetch_time))
        ]
        return entries

    def parse_line(self, line: str, fetch_time: datetime) -> Optional[PhishingEntry]:
        return PhishingEntry(url=line, source=self.FEED_TYPE, fetch_date=fetch_time)

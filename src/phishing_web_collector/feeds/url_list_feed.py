from datetime import datetime
from typing import List, Optional

from phishing_web_collector.feeds.file_based_feed import FileBasedFeed
from phishing_web_collector.models import PhishingEntry


class URLListFeedProvider(FileBasedFeed):
    """Abstract base class for URL list feed providers."""

    def parse_feed(self, raw_data: str) -> List[PhishingEntry]:
        """Parse the raw feed data and return a list of PhishingEntry objects."""
        fetch_time = datetime.now()
        entries = [
            entry
            for line in raw_data.splitlines()
            if line.strip() and not line.strip().startswith("#")
            if (entry := self.parse_line(line.strip(), fetch_time))
        ]
        return entries

    def parse_line(self, line: str, fetch_time: datetime) -> Optional[PhishingEntry]:
        """Parse a single line and return a PhishingEntry object."""
        return PhishingEntry(url=line, source=self.FEED_TYPE, fetch_date=fetch_time)

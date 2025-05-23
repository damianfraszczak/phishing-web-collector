from datetime import datetime
from typing import Dict, Optional

from phishing_web_collector.feeds.csv_feed import CSVFeedProvider
from phishing_web_collector.models import FeedSource, PhishingEntry
from phishing_web_collector.taxonomies import RefreshInterval


class PhishStatsFeed(CSVFeedProvider):
    URL = "https://phishstats.info/phish_score.csv"
    FEED_TYPE = FeedSource.PHISH_STATS
    INTERVAL = RefreshInterval.EVERY_2_HOURS.value
    DELIMITER = ","
    HEADERS = ["Date", "Score", "URL", "IP"]

    def parse_row(
        self, item: Dict[str, str], fetch_time: datetime
    ) -> Optional[PhishingEntry]:
        return PhishingEntry(
            url=item.get("URL"),
            source=self.FEED_TYPE,
            fetch_date=fetch_time,
        )

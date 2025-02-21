from datetime import datetime
from typing import Dict, Optional

from phishing_web_collector.feeds.csv_feed import CSVFeedProvider
from phishing_web_collector.models import FeedSource, PhishingEntry


class BotvrijFeed(CSVFeedProvider):
    URL = "https://www.botvrij.eu/data/blocklist/blocklist_domain.csv"
    FEED_TYPE = FeedSource.BOTVRIJ
    DELIMITER = ","

    def parse_row(
        self, item: Dict[str, str], fetch_time: datetime
    ) -> Optional[PhishingEntry]:
        return PhishingEntry(
            url=item["value"], source=self.FEED_TYPE, fetch_date=fetch_time
        )

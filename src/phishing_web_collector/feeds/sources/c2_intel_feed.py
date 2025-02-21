from datetime import datetime
from typing import Dict, Optional

from phishing_web_collector.feeds.csv_feed import CSVFeedProvider
from phishing_web_collector.models import FeedSource, PhishingEntry


class C2IntelFeed(CSVFeedProvider):
    URL = "https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/refs/heads/master/feeds/domainC2s.csv"
    FEED_TYPE = FeedSource.C2_INTEL_DOMAIN
    DELIMITER = ","

    def parse_row(
        self, item: Dict[str, str], fetch_time: datetime
    ) -> Optional[PhishingEntry]:
        domain = item.get("#domain")
        if not domain:
            return None
        return PhishingEntry(url=domain, source=self.FEED_TYPE, fetch_date=fetch_time)

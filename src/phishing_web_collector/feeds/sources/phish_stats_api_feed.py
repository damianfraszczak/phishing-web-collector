from datetime import datetime
from typing import Dict, Optional

from phishing_web_collector.feeds.json_feed import JSONFeed
from phishing_web_collector.models import FeedSource, PhishingEntry
from phishing_web_collector.taxonomies import RefreshInterval


class PhishStatsApiFeed(JSONFeed):
    URL = "https://api.phishstats.info/api/phishing?_sort=-id"
    FEED_TYPE = FeedSource.PHISH_STATS
    INTERVAL = RefreshInterval.HOURLY.value

    def parse_entry(self, item: Dict, fetch_time: datetime) -> Optional[PhishingEntry]:
        return PhishingEntry(
            url=item.get("url"),
            source=self.FEED_TYPE,
            fetch_date=fetch_time,
        )

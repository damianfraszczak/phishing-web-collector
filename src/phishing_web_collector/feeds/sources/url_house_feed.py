from datetime import datetime
from typing import Dict, Optional

from phishing_web_collector.feeds.csv_feed import CSVFeedProvider
from phishing_web_collector.models import FeedSource, PhishingEntry
from phishing_web_collector.taxonomies import RefreshInterval


class UrlHausFeed(CSVFeedProvider):
    URL = "https://urlhaus.abuse.ch/downloads/csv_recent/"
    FEED_TYPE = FeedSource.URL_HAUS
    INTERVAL = RefreshInterval.HOURLY.value
    DELIMITER = ","
    HEADERS = [
        "id",
        "dateadded",
        "url",
        "url_status",
        "last_online",
        "threat",
        "tags",
        "urlhaus_link",
        "reporter",
    ]

    def parse_row(
        self, item: Dict[str, str], fetch_time: datetime
    ) -> Optional[PhishingEntry]:
        return PhishingEntry(
            url=item["url"],
            source=self.FEED_TYPE,
            fetch_date=fetch_time,
            reference_url=item["urlhaus_link"],
        )

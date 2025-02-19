from datetime import datetime
from typing import Dict, Optional

from pwc.feeds.csv_feed import CSVFeedProvider
from pwc.models import FeedSource, PhishingEntry


class CertPLFeed(CSVFeedProvider):
    URL = "https://hole.cert.pl/domains/domains.csv"
    FEED_TYPE = FeedSource.CERT_PL
    DELIMITER = "\t"

    def parse_row(
        self, item: Dict[str, str], fetch_time: datetime
    ) -> Optional[PhishingEntry]:
        return PhishingEntry(
            url=item["AdresDomeny"], source=self.FEED_TYPE, fetch_date=fetch_time
        )

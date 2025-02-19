from datetime import datetime
from typing import Dict, Optional

from pwc.feeds.json_feed import JSONFeed
from pwc.models import FeedSource, PhishingEntry
from pwc.taxonomies import RefreshInterval


class PhishTankFeed(JSONFeed):
    """https://github.com/ProKn1fe/phishtank-database"""

    URL = "https://raw.githubusercontent.com/ProKn1fe/phishtank-database/master/online-valid.json"
    FEED_TYPE = FeedSource.PHISH_TANK
    INTERVAL = RefreshInterval.DAILY.value

    def parse_entry(
        self, item: Dict[str, str], fetch_time: datetime
    ) -> Optional[PhishingEntry]:
        return PhishingEntry(
            url=item["url"],
            targeted_url=item.get("phish_target"),
            reference_url=item.get("phish_detail_url"),
            source=self.FEED_TYPE,
            fetch_date=fetch_time,
        )

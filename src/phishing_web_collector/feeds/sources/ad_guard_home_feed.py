from datetime import datetime
from typing import Optional

from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource, PhishingEntry
from phishing_web_collector.taxonomies import RefreshInterval


class AdGuardHomeFeed(URLListFeedProvider):
    """Feed provider for AdGuard Home block list."""

    URL = "https://raw.githubusercontent.com/Ealenn/AdGuard-Home-List/gh-pages/AdGuard-Home-List.Block.txt"
    FEED_TYPE = FeedSource.AD_GUARD_HOME
    INTERVAL = RefreshInterval.DAILY.value

    def parse_line(self, line: str, fetch_time: datetime) -> Optional[PhishingEntry]:
        if line.startswith("||") and line.endswith("^"):
            url = line[2:-1].strip()
            return super().parse_line(url, fetch_time)
        return None

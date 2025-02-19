from datetime import datetime
from typing import Dict, Optional

from pwc.feeds.json_feed import JSONFeed
from pwc.models import FeedSource, PhishingEntry
from pwc.taxonomies import RefreshInterval


class TweetFeedProvider(JSONFeed):
    URL = "https://api.tweetfeed.live/v1/today/phishing/url"
    FEED_TYPE = FeedSource.TWEET_FEED
    INTERVAL = RefreshInterval.HOURLY.value

    def parse_entry(self, item: Dict, fetch_time: datetime) -> Optional[PhishingEntry]:
        """Extrac phishing URL and domain from API response."""
        url = item.get("value")
        reference_url = item.get("tweet")
        if not reference_url or not url:
            return None

        return PhishingEntry(
            url=url,
            reference_url=reference_url,
            source=self.FEED_TYPE,
            fetch_date=fetch_time,
        )

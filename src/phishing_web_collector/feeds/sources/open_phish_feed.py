from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class OpenPhishFeed(URLListFeedProvider):
    """Feed provider for OpenPhish phishing URL feed."""

    URL = "https://openphish.com/feed.txt"
    FEED_TYPE = FeedSource.OPEN_PHISH
    INTERVAL = RefreshInterval.EVERY_12_HOURS.value

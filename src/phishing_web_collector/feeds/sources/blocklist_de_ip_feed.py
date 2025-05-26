from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class BlockListDeIpFeed(URLListFeedProvider):
    URL = "https://lists.blocklist.de/lists/all.txt"
    FEED_TYPE = FeedSource.BLOCKLIST_DE_IP
    INTERVAL = RefreshInterval.DAILY.value

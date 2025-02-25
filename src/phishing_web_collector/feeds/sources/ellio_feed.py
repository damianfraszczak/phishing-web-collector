from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class EllioIpFeed(URLListFeedProvider):
    URL = "https://cdn.ellio.tech/community-feed"
    FEED_TYPE = FeedSource.ELLIO_IP
    INTERVAL = RefreshInterval.DAILY

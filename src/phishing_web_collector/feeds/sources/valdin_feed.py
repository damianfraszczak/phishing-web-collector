from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class ValdinFeed(URLListFeedProvider):
    URL = "https://raw.githubusercontent.com/MikhailKasimov/validin-phish-feed/refs/heads/main/validin-phish-feed.txt"
    FEED_TYPE = FeedSource.VALDIN
    INTERVAL = RefreshInterval.WEEKLY.value

from pwc.feeds.url_list_feed import URLListFeedProvider
from pwc.models import FeedSource
from pwc.taxonomies import RefreshInterval


class ValdinFeed(URLListFeedProvider):
    URL = "https://raw.githubusercontent.com/MikhailKasimov/validin-phish-feed/refs/heads/main/validin-phish-feed.txt"
    FEED_TYPE = FeedSource.VALDIN
    INTERVAL = RefreshInterval.WEEKLY

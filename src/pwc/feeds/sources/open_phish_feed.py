from pwc.feeds.url_list_feed import URLListFeedProvider
from pwc.models import FeedSource
from pwc.taxonomies import RefreshInterval


class OpenPhishFeed(URLListFeedProvider):
    URL = "https://openphish.com/feed.txt"
    FEED_TYPE = FeedSource.OPEN_PHISH
    INTERVAL = RefreshInterval.EVERY_12_HOURS.value

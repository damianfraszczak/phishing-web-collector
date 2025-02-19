from pwc.feeds.url_list_feed import URLListFeedProvider
from pwc.models import FeedSource


class ThreatViewFeed(URLListFeedProvider):
    URL = "https://threatview.io/Downloads/DOMAIN-High-Confidence-Feed.txt"
    FEED_TYPE = FeedSource.PHISHING_ARMY

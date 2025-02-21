from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource


class ThreatViewFeed(URLListFeedProvider):
    URL = "https://threatview.io/Downloads/DOMAIN-High-Confidence-Feed.txt"
    FEED_TYPE = FeedSource.PHISHING_ARMY

from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource


class ThreatViewFeed(URLListFeedProvider):
    """Feed provider for ThreatView high-confidence domain feed."""

    URL = "https://threatview.io/Downloads/DOMAIN-High-Confidence-Feed.txt"
    FEED_TYPE = FeedSource.PHISHING_ARMY

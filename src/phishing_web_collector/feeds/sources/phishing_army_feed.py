from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource


class PhishingArmyFeed(URLListFeedProvider):
    """Feed provider for Phishing Army blocklist."""

    URL = "https://phishing.army/download/phishing_army_blocklist.txt"
    FEED_TYPE = FeedSource.PHISHING_ARMY

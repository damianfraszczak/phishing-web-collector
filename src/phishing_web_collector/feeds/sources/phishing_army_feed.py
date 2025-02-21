from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource


class PhishingArmyFeed(URLListFeedProvider):
    URL = "https://phishing.army/download/phishing_army_blocklist.txt"
    FEED_TYPE = FeedSource.PHISHING_ARMY

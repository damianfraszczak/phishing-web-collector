from pwc.feeds.url_list_feed import URLListFeedProvider
from pwc.models import FeedSource


class PhishingArmyFeed(URLListFeedProvider):
    URL = "https://phishing.army/download/phishing_army_blocklist.txt"
    FEED_TYPE = FeedSource.PHISHING_ARMY

from pwc.feeds.url_list_feed import URLListFeedProvider
from pwc.models import FeedSource
from pwc.taxonomies import RefreshInterval


class PhishingDatabaseFeed(URLListFeedProvider):
    URL = "https://raw.githubusercontent.com/Phishing-Database/Phishing.Database/refs/heads/master/phishing-domains-ACTIVE.txt"
    FEED_TYPE = FeedSource.PHISHING_DATABASE
    INTERVAL = RefreshInterval.DAILY

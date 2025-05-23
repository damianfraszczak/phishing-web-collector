from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class PhishingDatabaseFeed(URLListFeedProvider):
    URL = "https://raw.githubusercontent.com/Phishing-Database/Phishing.Database/refs/heads/master/phishing-domains-ACTIVE.txt"
    FEED_TYPE = FeedSource.PHISHING_DATABASE
    INTERVAL = RefreshInterval.DAILY.value

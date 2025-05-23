from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class BinaryDefenceIpFeed(URLListFeedProvider):
    URL = "https://www.binarydefense.com/banlist.txt"
    FEED_TYPE = FeedSource.BINARY_DEFENCE_IP
    INTERVAL = RefreshInterval.DAILY.value

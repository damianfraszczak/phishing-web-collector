from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class MiraiSecurityIpFeed(URLListFeedProvider):
    URL = "https://mirai.security.gives/data/ip_list.txt"
    FEED_TYPE = FeedSource.MIRAI_SECURITY_IP
    INTERVAL = RefreshInterval.DAILY.value

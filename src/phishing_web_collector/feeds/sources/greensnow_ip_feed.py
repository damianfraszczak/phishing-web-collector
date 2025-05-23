from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class GreenSnowIpFeed(URLListFeedProvider):
    URL = "https://blocklist.greensnow.co/greensnow.txt"
    FEED_TYPE = FeedSource.GREEN_SNOW_IP
    INTERVAL = RefreshInterval.DAILY.value

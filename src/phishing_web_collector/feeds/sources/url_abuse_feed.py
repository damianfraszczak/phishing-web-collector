from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class UrlAbuseFeed(URLListFeedProvider):
    URL = "https://urlabuse.com/public/data/phishing_url.txt"
    FEED_TYPE = FeedSource.URL_ABUSE
    INTERVAL = RefreshInterval.HOURLY.value

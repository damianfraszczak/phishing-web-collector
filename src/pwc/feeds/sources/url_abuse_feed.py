from pwc.feeds.url_list_feed import URLListFeedProvider
from pwc.models import FeedSource
from pwc.taxonomies import RefreshInterval


class UrlAbuseFeed(URLListFeedProvider):
    URL = "https://urlabuse.com/public/data/phishing_url.txt"
    FEED_TYPE = FeedSource.URL_ABUSE
    INTERVAL = RefreshInterval.HOURLY

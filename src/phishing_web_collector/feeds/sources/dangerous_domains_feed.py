from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class DangerousDomainsFeed(URLListFeedProvider):
    """Feed provider for Dangerous Domains list."""

    URL = "https://dangerous.domains/list.txt"
    FEED_TYPE = FeedSource.DANGEROUS_DOMAINS
    INTERVAL = RefreshInterval.EVERY_6_HOURS.value

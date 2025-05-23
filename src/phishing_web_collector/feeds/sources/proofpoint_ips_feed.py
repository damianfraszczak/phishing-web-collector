from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class ProofPointIpFeed(URLListFeedProvider):
    URL = "https://rules.emergingthreats.net/blockrules/compromised-ips.txt"
    FEED_TYPE = FeedSource.PROOF_POINT_IP
    INTERVAL = RefreshInterval.DAILY.value

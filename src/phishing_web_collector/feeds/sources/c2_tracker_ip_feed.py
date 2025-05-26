from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource
from phishing_web_collector.taxonomies import RefreshInterval


class C2TrackerIpFeed(URLListFeedProvider):
    URL = "https://github.com/montysecurity/C2-Tracker/blob/main/data/all.txt"
    FEED_TYPE = FeedSource.C2_TRACKER_IP
    INTERVAL = RefreshInterval.WEEKLY.value

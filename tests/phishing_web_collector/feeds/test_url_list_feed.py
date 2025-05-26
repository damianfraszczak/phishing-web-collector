from datetime import datetime

import pytest

from phishing_web_collector.feeds.url_list_feed import URLListFeedProvider
from phishing_web_collector.models import FeedSource, PhishingEntry


class DummyFeed(URLListFeedProvider):
    FEED_TYPE = FeedSource.PHISH_STATS


@pytest.fixture
def provider():
    return DummyFeed("dummy_path")


def test_parse_feed_skips_comments(provider):
    raw = "# comment\nhttp://malicious.com\n\n# another comment\nhttp://phish.com"
    result = provider.parse_feed(raw)
    assert len(result) == 2
    assert result[0].url == "http://malicious.com"
    assert result[1].url == "http://phish.com"


def test_parse_feed_empty(provider):
    raw = "# only comment\n\n  \n"
    result = provider.parse_feed(raw)
    assert result == []


def test_parse_line_returns_entry(provider):
    now = datetime.now()
    entry = provider.parse_line("http://malicious.com", now)
    assert isinstance(entry, PhishingEntry)
    assert entry.url == "http://malicious.com"
    assert entry.source == FeedSource.PHISH_STATS
    assert entry.fetch_date == now

import json
from datetime import datetime
from unittest.mock import AsyncMock, patch

import pytest

from phishing_web_collector.feeds.sources.tweet_feed_feed import TweetFeed
from phishing_web_collector.models import FeedSource, PhishingEntry


@pytest.fixture
def provider():
    return TweetFeed("mock_path")


@pytest.mark.asyncio
@patch("phishing_web_collector.feeds.file_based_feed.fetch_url", new_callable=AsyncMock)
async def test_tweet_feed_parse(mock_fetch, provider):
    mock_data = [
        {"value": "http://malicious.com", "tweet": "https://twitter.com/example"},
        {"value": "http://bad.com", "tweet": "https://twitter.com/abc"},
        {"value": None, "tweet": "https://twitter.com/missing"},
        {"value": "http://no-tweet.com", "tweet": None},
    ]
    mock_fetch.return_value = json.dumps(mock_data)

    result = await provider.fetch_feed()
    entries = provider.parse_feed(result)

    assert len(entries) == 2
    assert all(isinstance(e, PhishingEntry) for e in entries)
    assert entries[0].url == "http://malicious.com"
    assert entries[0].reference_url == "https://twitter.com/example"
    assert entries[0].source == FeedSource.TWEET_FEED


def test_tweet_feed_parse_entry_valid(provider):
    fetch_time = datetime.now()
    item = {"value": "http://phishing.com", "tweet": "https://twitter.com/test"}
    entry = provider.parse_entry(item, fetch_time)

    assert isinstance(entry, PhishingEntry)
    assert entry.url == "http://phishing.com"
    assert entry.reference_url == "https://twitter.com/test"
    assert entry.source == FeedSource.TWEET_FEED


@pytest.mark.parametrize(
    "item",
    [
        {"value": None, "tweet": "https://twitter.com"},
        {"value": "http://x.com", "tweet": None},
        {"value": None, "tweet": None},
    ],
)
def test_tweet_feed_parse_entry_invalid(provider, item):
    fetch_time = datetime.now()
    entry = provider.parse_entry(item, fetch_time)
    assert entry is None

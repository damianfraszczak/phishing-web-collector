from unittest.mock import AsyncMock, patch

import pytest

from phishing_web_collector import OpenPhishFeed
from phishing_web_collector.models import FeedSource, PhishingEntry


@pytest.fixture
def provider():
    return OpenPhishFeed("mock_path")


@pytest.mark.asyncio
@patch("phishing_web_collector.feeds.file_based_feed.fetch_url", new_callable=AsyncMock)
async def test_openphish_feed_parse(mock_fetch, provider):
    raw_data = "1.6.224.122\n1.15.173.165\n# Comment line\n\n"
    mock_fetch.return_value = raw_data

    result = await provider.fetch_feed()
    entries = provider.parse_feed(result)

    assert len(entries) == 2
    assert isinstance(entries[0], PhishingEntry)
    assert entries[0].url == "1.6.224.122"
    assert entries[0].source == FeedSource.OPEN_PHISH
    assert entries[1].url == "1.15.173.165"

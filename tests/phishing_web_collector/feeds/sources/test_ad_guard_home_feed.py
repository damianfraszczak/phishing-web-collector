from datetime import datetime
from unittest.mock import AsyncMock, patch

import pytest

from phishing_web_collector import AdGuardHomeFeed
from phishing_web_collector.models import PhishingEntry
from phishing_web_collector.taxonomies import FeedSource


@pytest.fixture
def provider():
    return AdGuardHomeFeed("mock_path")


@pytest.mark.asyncio
@patch("phishing_web_collector.feeds.file_based_feed.fetch_url", new_callable=AsyncMock)
async def test_adguard_home_feed_parse(mock_fetch, provider):
    raw_data = "||malicious.com^\n||bad-site.org^\ninvalidline\n\n"
    mock_fetch.return_value = raw_data

    result = await provider.fetch_feed()
    entries = provider.parse_feed(result)

    assert len(entries) == 2
    assert all(isinstance(e, PhishingEntry) for e in entries)
    assert entries[0].url == "malicious.com"
    assert entries[0].source == FeedSource.AD_GUARD_HOME
    assert entries[1].url == "bad-site.org"


def test_adguard_home_feed_parse_line_valid(provider):
    fetch_time = datetime.now()
    entry = provider.parse_line("||test-site.com^", fetch_time)

    assert isinstance(entry, PhishingEntry)
    assert entry.url == "test-site.com"
    assert entry.source == FeedSource.AD_GUARD_HOME


def test_adguard_home_feed_parse_line_invalid(provider):
    fetch_time = datetime.now()
    entry = provider.parse_line("not-a-valid-line", fetch_time)

    assert entry is None

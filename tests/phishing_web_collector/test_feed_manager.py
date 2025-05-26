from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

from phishing_web_collector import FeedManager
from phishing_web_collector.models import FeedSource, PhishingEntry


@pytest.fixture
def mock_feed():
    async def mock_refresh(force):
        return None

    mock = MagicMock()
    mock.refresh = mock_refresh
    mock.retrieve.return_value = [
        PhishingEntry(
            url="http://test.com",
            targeted_url="http://target.com",
            reference_url="http://ref.com",
            source=FeedSource.PHISH_TANK,
            fetch_date=datetime.now(),
        )
    ]
    return mock


@pytest.fixture
def feed_manager(mock_feed):
    with patch(
        "phishing_web_collector.feed_manager.SOURCES_MAP",
        {FeedSource.PHISH_TANK: lambda path: mock_feed},
    ):
        return FeedManager([FeedSource.PHISH_TANK], "mock_path")


@pytest.mark.asyncio
async def test_retrieve_all(feed_manager):
    entries = await feed_manager.retrieve_all()
    assert len(entries) == 1
    assert entries[0].url == "http://test.com"


def test_sync_retrieve_all(feed_manager):
    entries = feed_manager.sync_retrieve_all()
    assert len(entries) == 1
    assert entries[0].url == "http://test.com"


def test_entry_map(feed_manager):
    feed_manager.entries = [
        PhishingEntry(
            url="http://test.com",
            targeted_url="http://target.com",
            reference_url="http://ref.com",
            source=FeedSource.PHISH_TANK,
            fetch_date=datetime.now(),
        )
    ]
    result = feed_manager.entry_map
    assert "http://test.com" in result
    assert isinstance(result["http://test.com"], list)


def test_export_to_json(feed_manager, tmp_path):
    test_file = tmp_path / "output.json"
    feed_manager.entries = [
        PhishingEntry(
            url="http://test.com",
            targeted_url="http://target.com",
            reference_url="http://ref.com",
            source=FeedSource.PHISH_TANK,
            fetch_date=datetime.now(),
        )
    ]
    feed_manager.export_to_json(str(test_file))
    assert test_file.exists()
    assert test_file.read_text()


def test_load_from_json(feed_manager):
    mock_data = {
        "http://test.com": [
            {
                "targeted_url": "http://target.com",
                "reference_url": "http://ref.com",
                "source": "PhishTank",
                "fetch_date": "2024-05-01T10:00:00",
            }
        ]
    }

    with patch("phishing_web_collector.feed_manager.load_json", return_value=mock_data):
        feed_manager.load_from_json("mock.json")

        assert len(feed_manager.entries) == 1
        assert feed_manager.entries[0].url == "http://test.com"


def test_find_entry(feed_manager):
    now = datetime.now()
    feed_manager.entries = [
        PhishingEntry(
            url="http://findme.com",
            targeted_url="http://target.com",
            reference_url="http://ref.com",
            source=FeedSource.PHISH_TANK,
            fetch_date=now,
        )
    ]
    found = feed_manager.find_entry("http://findme.com")
    assert isinstance(found, list)
    assert found[0]["targeted_url"] == "http://target.com"

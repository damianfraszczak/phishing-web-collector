import json

import pytest

from phishing_web_collector.feeds.json_feed import JSONFeed
from phishing_web_collector.models import FeedSource, PhishingEntry


class DummyJSONFeed(JSONFeed):
    FEED_TYPE = FeedSource.PHISH_TANK

    def parse_entry(self, item, fetch_time):
        if "url" in item:
            return PhishingEntry(
                url=item["url"],
                targeted_url=item.get("targeted_url"),
                reference_url=item.get("reference_url"),
                source=self.FEED_TYPE,
                fetch_date=fetch_time,
            )
        return None


@pytest.fixture
def provider():
    return DummyJSONFeed("dummy_path")


def test_parse_feed_valid_json(provider):
    raw_data = json.dumps(
        [
            {
                "url": "http://phish.com",
                "targeted_url": "http://target.com",
                "reference_url": "http://ref.com",
            }
        ]
    )
    result = provider.parse_feed(raw_data)
    assert len(result) == 1
    assert result[0].url == "http://phish.com"


def test_parse_feed_invalid_json(provider, caplog):
    raw_data = "{invalid json}"
    result = provider.parse_feed(raw_data)
    assert result == []
    assert any("Failed to parse JSON" in msg for msg in caplog.text.splitlines())


def test_parse_feed_entry_returns_none(provider):
    raw_data = json.dumps([{"invalid": "data"}])
    result = provider.parse_feed(raw_data)
    assert result == []

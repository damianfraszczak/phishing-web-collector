from unittest.mock import patch

import pytest


@pytest.fixture(autouse=True, scope="session")
def mock_path_mkdir():
    with patch("phishing_web_collector.feeds.feed.Path.mkdir") as mock_mkdir:
        yield mock_mkdir

from unittest import mock

import pytest

from phishing_web_collector.utils import (
    fetch_url,
    get_domain_from_url,
    get_ip_from_domain,
    get_ip_from_url,
    remove_none_from_dict,
    run_async_as_sync,
    valid_ip,
)


def test_valid_ip_valid():
    assert valid_ip("192.168.0.1") is True
    assert valid_ip("::1") is True


def test_valid_ip_invalid():
    assert valid_ip("not_an_ip") is False
    assert valid_ip("256.256.256.256") is False


def test_get_domain_from_url_with_scheme():
    assert get_domain_from_url("https://example.com/test") == "example.com"


def test_get_domain_from_url_without_scheme():
    assert get_domain_from_url("example.com/test") == "example.com"


@mock.patch("socket.gethostbyname", return_value="93.184.216.34")
def test_get_ip_from_domain(mock_gethostbyname):
    assert get_ip_from_domain("example.com") == "93.184.216.34"


@mock.patch("socket.gethostbyname", return_value="93.184.216.34")
def test_get_ip_from_url(mock_gethostbyname):
    assert get_ip_from_url("http://example.com") == "93.184.216.34"


def test_remove_none_from_dict():
    input_data = {
        "a": 1,
        "b": None,
        "c": {"d": None, "e": 2},
        "f": [1, None, {"g": None, "h": 3}],
    }
    expected = {"a": 1, "c": {"e": 2}, "f": [1, None, {"h": 3}]}
    assert remove_none_from_dict(input_data) == expected


@pytest.mark.asyncio
async def test_fetch_url_failure(monkeypatch):
    class FailingSession:
        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            pass

        async def get(self, url, headers):
            raise Exception("Network error")

    monkeypatch.setattr(
        "aiohttp.ClientSession", lambda *args, **kwargs: FailingSession()
    )

    content = await fetch_url("http://example.com")
    assert content is None


async def async_add(x, y):
    return x + y


def test_run_async_as_sync():
    result = run_async_as_sync(async_add, 3, 4)
    if hasattr(result, "__await__"):
        # If running in Jupyter (event loop running), we need to await result
        import asyncio

        result = asyncio.get_event_loop().run_until_complete(result)
    assert result == 7

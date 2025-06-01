import ipaddress
import json
import logging
import socket
import ssl
from urllib.parse import urlparse

import aiohttp
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)

DEFAULT_HEADERS = {"User-Agent": "Mozilla/5.0"}


def valid_ip(host: str) -> bool:
    """Check if the given host is a valid IP address."""
    try:
        ipaddress.ip_address(host)
        return True
    except Exception as e:  # noqa
        logger.warn(e)
        return False


def get_domain_from_url(url: str) -> str:
    """Extract the domain from the URL. If no scheme is provided, assume 'http://'."""
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    parsed_url = urlparse(url)
    return parsed_url.netloc


def get_ip_from_domain(domain: str) -> str:
    """Return the IP address for the given domain."""
    return socket.gethostbyname(domain)


def get_ip_from_url(url: str) -> str:
    """Return the IP address for the given URL."""
    return get_ip_from_domain(get_domain_from_url(url))


def remove_none_from_dict(d):
    """Recursively remove keys with None values from a dictionary."""
    if isinstance(d, dict):
        return {k: remove_none_from_dict(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [remove_none_from_dict(i) for i in d]
    else:
        return d


async def fetch_url(url, headers=None, ssl_verify=False, timeout=10):
    """Fetch the given URL and return the response text or None on failure."""
    headers = {**DEFAULT_HEADERS, **(headers or {})}

    ssl_context = None
    if not ssl_verify:
        ssl_context = ssl._create_unverified_context()  # nosec B323

    timeout_obj = aiohttp.ClientTimeout(total=timeout)
    connector = aiohttp.TCPConnector(ssl=ssl_context)

    try:
        async with aiohttp.ClientSession(
            connector=connector, timeout=timeout_obj
        ) as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    return await response.text(encoding="utf-8")
                logger.warning(f"Failed to fetch {url} - Status: {response.status}")
    except Exception as e:  # noqa
        logger.error(f"Error fetching {url}: {e}")

    return None


def fetch_url_sync(url, headers=None, ssl_verify=False, timeout=10):
    """Fetch the given URL synchronously and return the response text or None on failure."""
    headers = {**DEFAULT_HEADERS, **(headers or {})}
    try:
        response = requests.get(
            url, headers=headers, verify=ssl_verify, timeout=timeout
        )
        if response.status_code == 200:
            return response.text
        logger.warning(f"Failed to fetch {url} - Status: {response.status_code}")
    except Exception as e:  # noqa
        logger.error(f"Error fetching {url}: {e}")
    return None


def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

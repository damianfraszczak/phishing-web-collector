import ipaddress
import logging
import socket
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


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
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    parsed_url = urlparse(url)
    return parsed_url.netloc


def get_ip_from_domain(domain: str) -> str:
    """Return the IP address for the given domain."""
    return socket.gethostbyname(domain)


def get_ip_from_url(url: str) -> str:
    """Return the IP address for the given URL."""
    return get_ip_from_domain(get_domain_from_url(url))

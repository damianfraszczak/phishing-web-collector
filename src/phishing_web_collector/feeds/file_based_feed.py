import logging
from typing import Optional

from phishing_web_collector.utils import fetch_url
from phishing_web_collector.feeds.feed import AbstractFeed

logger = logging.getLogger(__name__)


class FileBasedFeed(AbstractFeed):
    URL: str

    async def fetch_feed(self) -> Optional[str]:
        """Fetch data from a URL and ensures the response is valid."""
        try:
            return await fetch_url(self.URL)
        except Exception as e:  # noqa
            logger.error(f"Error fetching {self.FEED_TYPE.value}: {e}")
            return None

import logging
from typing import Optional

import aiohttp

from pwc.feeds.feed import AbstractFeed

logger = logging.getLogger(__name__)


class FileBasedFeed(AbstractFeed):
    URL: str

    async def fetch_feed(self) -> Optional[str]:
        """Fetch data from a URL and ensures the response is valid."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.URL) as response:
                    if response.status == 200:
                        return await response.text(encoding="utf-8")
                    logger.warning(
                        f"Failed to fetch {self.FEED_TYPE.value} - Status: {response.status}"
                    )
                    return None
        except Exception as e:  # noqa
            logger.error(f"Error fetching {self.FEED_TYPE.value}: {e}")
            return None

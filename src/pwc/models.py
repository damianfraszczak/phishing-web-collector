from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.pwc.taxonomies import FeedSource


@dataclass
class PhishingEntry:
    url: str
    source: FeedSource
    fetch_date: datetime
    targeted_url: Optional[str] = None
    reference_url: Optional[str] = None


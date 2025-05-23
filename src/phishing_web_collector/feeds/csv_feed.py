import csv
from abc import abstractmethod
from datetime import datetime
from io import StringIO
from typing import Dict, List, Optional

from phishing_web_collector.feeds.file_based_feed import FileBasedFeed
from phishing_web_collector.models import PhishingEntry


class CSVFeedProvider(FileBasedFeed):
    DELIMITER = ";"
    FILE_EXTENSION = "csv"
    HEADERS = None

    def parse_feed(self, raw_data: str) -> List[PhishingEntry]:
        entries = []
        raw_data_clean = [
            line.replace('"', "")
            for line in StringIO(raw_data).read().splitlines()
            if not line.startswith("#") and line.strip()
        ]
        reader = csv.DictReader(
            raw_data_clean, delimiter=self.DELIMITER, fieldnames=self.HEADERS
        )
        fetch_time = datetime.utcnow()

        for row in reader:
            entry = self.parse_row(row, fetch_time)
            if entry:
                entries.append(entry)

        return entries

    @abstractmethod
    def parse_row(
        self, row: Dict[str, str], fetch_time: datetime
    ) -> Optional[PhishingEntry]:
        pass

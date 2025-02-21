from enum import Enum

class FeedSource(Enum):
    PHISH_TANK = "PhishTank"
    OPEN_PHISH = "OpenPhish"
    TWEET_FEED = "TweetFeed"
    PHISHING_ARMY = "PhishingArmy"
    URL_ABUSE = "UrlAbuse"
    CERT_PL = "CertPl"
    THREAT_VIEW_DOMAIN = "ThreatViewDomain"
    C2_INTEL_DOMAIN = "C2IntelDomain"
    BOTVRIJ = "Botvrij"
    VALDIN = "Valdin"
    PHISHING_DATABASE = "PhishingDatabase"


class RefreshInterval(Enum):
    HOURLY = 3600
    EVERY_6_HOURS = 21600
    EVERY_12_HOURS = 43200
    DAILY = 86400
    WEEKLY = 604800


from enum import Enum


class FeedSource(Enum):
    BINARY_DEFENCE_IP = "BinaryDefenceIP"
    BLOCKLIST_DE_IP = "BlocklistDeIP"
    BOTVRIJ = "Botvrij"
    C2_INTEL_DOMAIN = "C2IntelDomain"
    C2_TRACKER_IP = "C2TrackerIp"
    CERT_PL = "CertPl"
    # ELLIO_IP = "EllioIP"
    GREEN_SNOW_IP = "GreenSnowIp"
    MIRAI_SECURITY_IP = "MiraiSecurityIp"
    OPEN_PHISH = "OpenPhish"
    PHISHING_ARMY = "PhishingArmy"
    PHISHING_DATABASE = "PhishingDatabase"
    PHISH_STATS = "PhishStats"
    PHISH_STATS_API = "PhishStatsApi"
    PHISH_TANK = "PhishTank"
    PROOF_POINT_IP = "ProofPointIp"
    THREAT_VIEW_DOMAIN = "ThreatViewDomain"
    TWEET_FEED = "TweetFeed"
    URL_ABUSE = "UrlAbuse"
    URL_HAUS = "UrlHaus"
    VALDIN = "Valdin"


class RefreshInterval(Enum):
    HOURLY = 3600
    EVERY_2_HOURS = 7200
    EVERY_6_HOURS = 21600
    EVERY_12_HOURS = 43200
    DAILY = 86400
    WEEKLY = 604800

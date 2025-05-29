import csv

import phishing_web_collector as pwc

manager = pwc.FeedManager(
    sources=[
        pwc.FeedSource.BINARY_DEFENCE_IP,
        pwc.FeedSource.BLOCKLIST_DE_IP,
        pwc.FeedSource.BOTVRIJ,
        pwc.FeedSource.C2_INTEL_DOMAIN,
        pwc.FeedSource.C2_TRACKER_IP,
        pwc.FeedSource.CERT_PL,
        pwc.FeedSource.DANGEROUS_DOMAINS,
        pwc.FeedSource.GREEN_SNOW_IP,
        pwc.FeedSource.MIRAI_SECURITY_IP,
        pwc.FeedSource.OPEN_PHISH,
        pwc.FeedSource.PHISHING_ARMY,
        pwc.FeedSource.PHISHING_DATABASE,
        pwc.FeedSource.PHISH_STATS_API,
        pwc.FeedSource.PHISH_TANK,
        pwc.FeedSource.PROOF_POINT_IP,
        pwc.FeedSource.THREAT_VIEW_DOMAIN,
        pwc.FeedSource.TWEET_FEED,
        pwc.FeedSource.URL_ABUSE,
        pwc.FeedSource.URL_HAUS,
        pwc.FeedSource.VALDIN,
    ],
    storage_path="feeds_data",
)

manager.sync_refresh_all()
entries = manager.sync_retrieve_all()

phishing_domains = [pwc.get_domain_from_url(item.url) for item in entries]

with open("phishing_domains.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Domain"])
    for domain in phishing_domains:
        writer.writerow([domain])

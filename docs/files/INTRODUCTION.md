# PhishingWebCollector: A Python Library for Phishing Website Collection

## Overview
`PhishingWebCollector` is a Python library that integrates 20 phishing feeds into one solution and offers a platform for collecting and managing malicious website data.
Suitable for practical cybersecurity applications, like updating local blacklists, and research, such as building phishing detection datasets.
It utilizes the asyncio module for efficient parallel processing and data collection.
Users can gather historical data from free feeds to construct extensive datasets without costly API subscriptions.
Its ease of use, scalability, and support for various data formats enhance the threat detection capabilities of cybersecurity teams and researchers while minimizing technical overhead.


## Features
- Integration of 22 Different Sources: Reduces the need to maintain multiple integrations.
- Local Data Collection: Supports building and maintaining local phishing databases.
- Data Export: Allows exporting all collected data in a unified JSON format.
- Asynchronous Performance: Uses asyncio for faster, simultaneous data collection.

### Integrations
- [AdGuardHome](https://raw.githubusercontent.com/Ealenn/AdGuard-Home-List/gh-pages/AdGuard-Home-List.Block.txt)
- [BinaryDefence](https://www.binarydefense.com/banlist.txt)
- [BlockListDe](https://lists.blocklist.de/lists/all.txt)
- [Botvrij](https://www.botvrij.eu/data/blocklist/blocklist_domain.csv)
- [C2IntelFeeds](https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/refs/heads/master/feeds/domainC2s.csv)
- [C2Tracker](https://github.com/montysecurity/C2-Tracker/blob/main/data/all.txt)
- [CertPL](https://hole.cert.pl/domains/domains.csv)
- [DangerousDomains](https://dangerous.domains/list.txt)
- [GreenSnow](https://blocklist.greensnow.co/greensnow.txt)
- [MalwareWorld](https://malwareworld.com/textlists/blacklists.txt)
- [MiraiSecurity](https://mirai.security.gives/data/ip_list.txt)
- [OpenPhish](https://openphish.com/feed.txt)
- [PhishTank](https://raw.githubusercontent.com/ProKn1fe/phishtank-database/master/online-valid.json)
- [PhishingArmy](https://phishing.army/download/phishing_army_blocklist.txt)
- [PhishingDatabase](https://raw.githubusercontent.com/Phishing-Database/Phishing.Database/refs/heads/master/phishing-domains-ACTIVE.txt)
- [PhishStats](https://api.phishstats.info/api/phishing)
- [Proofpoint](https://rules.emergingthreats.net/blockrules/compromised-ips.txt)
- [ThreatView](https://threatview.io/Downloads/DOMAIN-High-Confidence-Feed.txt)
- [TweetFeed](https://api.tweetfeed.live/v1/today/phishing/url)
- [URLAbuse](https://urlabuse.com/public/data/phishing_url.txt)
- [URLHaus](https://urlhaus.abuse.ch/downloads/csv_recent/)
- [Valdin](https://raw.githubusercontent.com/MikhailKasimov/validin-phish-feed/refs/heads/main/validin-phish-feed.txt)

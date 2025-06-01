<p align="center"><img src=".github/images/logo.png" width="256" alt="PhishingWebCollector" title="PhishingWebCollector"/></p>

<h1 align="center">
    ⚔️ PhishingWebCollector: A Python Library for Phishing Website Collection ⚔️
</h1>

<p align="center">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/phishing-web-collector.svg">
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/phishing-web-collector.svg" href="https://pepy.tech/project/phishing-web-collector">
    <a href="https://repology.org/project/python:phishing-web-collector/versions">
        <img src="https://repology.org/badge/tiny-repos/python:phishing-web-collector.svg" alt="Packaging status">
    </a>
    <img alt="Downloads" src="https://pepy.tech/badge/phishing-web-collector">
    <img alt="GitHub license" src="https://img.shields.io/github/license/damianfraszczak/phishing-web-collector.svg" href="https://github.com/damianfraszczak/phishing-web-collector/blob/master/LICENSE">
    <img alt="Documentation Status" src="https://readthedocs.org/projects/phishingwebcollector/badge/?version=latest" href="https://phishingwebcollector.readthedocs.io/en/latest/?badge=latest">
</p>

<p align="center">
  <a href="https://github.com/damianfraszczak/phishing-web-collector?tab=readme-ov-file#why-PhishingWebCollector">✨ Why PhishingWebCollector?</a>
  <a href="https://github.com/damianfraszczak/phishing-web-collector?tab=readme-ov-file#features">📦 Features</a>
  <a href="https://github.com/damianfraszczak/phishing-web-collector/blob/master/docs/files/QUICK_START.md">🚀 Quick Start</a>
  <a href="https://phishingwebcollector.readthedocs.io/">📮 Documentation</a>
  <a href="https://github.com/damianfraszczak/phishing-web-collector/blob/master/docs/files/jupyter">📓 Jupyter Notebook examples</a>
  <a href="LICENSE">🔑 License</a>
</p>


## Overview
`PhishingWebCollector` is a Python library that integrates 20 phishing feeds into one solution and offers a platform for collecting and managing malicious website data.
Suitable for practical cybersecurity applications, like updating local blacklists, and research, such as building phishing detection datasets.
It utilizes the asyncio module for efficient parallel processing and data collection.
Users can gather historical data from free feeds to construct extensive datasets without costly API subscriptions.
Its ease of use, scalability, and support for various data formats enhance the threat detection capabilities of cybersecurity teams and researchers while minimizing technical overhead.



* **Free software:** MIT license,
* **Python versions:** 3.9 | 3.10 | 3.11
* **Tested OS:** Windows, Ubuntu, Fedora and CentOS. **However, that does not mean it does not work on others.**
* **All-in-One Solution::**  PhishingWebCollector is an all-in-one solution that allows for the collection of a wide range of information about websites.
* **Efficiency and Expertise: :** Building a similar solution independently would be very time-consuming and require specialized knowledge.
* **Open Source Advantage: :** Publishing this tool as open source will facilitate many studies, making them simpler and allowing researchers and industry professionals to focus on more advanced tasks.
* **Continuous Improvement: :** New techniques will be added successively, ensuring continuous growth in this area.

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

## Why PhishingWebCollector?
While many tools and scripts can collect phishing data, none offer a complete all-in-one solution like `PhishingWebCollector`. It combines comprehensive functionality with high performance, asynchronous data collection, and easy configuration, making it both efficient and user-friendly.


## How to use
Library can be installed using pip:

```bash
pip install phishing-web-collector
```

## Code usage

### Getting all phishing domains from all available sources

```python
import phishing_web_collector as pwc

manager = pwc.FeedManager(
    sources=list(pwc.FeedSource),
    storage_path="feeds_data"
)

manager.sync_refresh_all()
entries = manager.sync_retrieve_all()

phishing_domains = [pwc.get_domain_from_url(item.url) for item in entries]

for domain in phishing_domains:
    print(domain)

```
and as a results you will get the list of phishing domains.

All modules are exported into main package, so you can use import module and invoke them directly.

## Jupyter Notebook Usage
If you would like to test ``PhishingWebCollector`` functionalities without installing it on your machine consider using the preconfigured [Jupyter notebook](docs/files/jupyter/collect_phishing_domains.ipynb). It will show you how to collect phishing domains from all available sources and save them into a CSV file. You can run it in your browser without any installation using [Google Colab](https://colab.research.google.com/github/damianfraszczak/phishing-web-collector/blob/master/docs/files/jupyter/collect_phishing_domains.ipynb).

To check how asynchronous data collection is faster than synchronous one, you can run the [asynchronous benchmark notebook](docs/files/jupyter/sync_vs_async_benchmark.ipynb).

To check how to run feeds directly, you can run the [direct feed invocation notebook](docs/files/jupyter/direct_feed_invocation.ipynb).

## Docker usage
If you want to use `PhishingWebCollector` in a Docker container, please check this [README](docs/files/docker/README.md) file.

## Contributing

For contributing, refer to its [CONTRIBUTING.md](.github/CONTRIBUTING.md) file.
We are a welcoming community... just follow the [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## Maintainers

Project maintainers are:

- Damian Frąszczak
- Edyta Frąszczak

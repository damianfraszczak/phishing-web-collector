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
    <img alt="Documentation Status" src="https://readthedocs.org/projects/phishing-web-collector/badge/?version=latest" href="https://phishing-web-collector.readthedocs.io/en/latest/?badge=latest">
</p>

<p align="center">
  <a href="https://github.com/damianfraszczak/phishing-web-collector?tab=readme-ov-file#why-PhishingWebCollector">✨ Why PhishingWebCollector?</a>
  <a href="https://github.com/damianfraszczak/phishing-web-collector?tab=readme-ov-file#features">📦 Features</a>
  <a href="https://github.com/damianfraszczak/phishing-web-collector/blob/master/docs/files/QUICK_START.md">🚀 Quick Start</a>
   <a href="https://phishing-web-collector.readthedocs.io/">📮 Documentation</a>
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
* **Documentation:** https://phishing-web-collector.readthedocs.io/en/latest/,
* **Python versions:** 3.9 | 3.10 | 3.11
* **Tested OS:** Windows, Ubuntu, Fedora and CentOS. **However, that does not mean it does not work on others.**
* **All-in-One Solution::**  PhishingWebCollector is an all-in-one solution that allows for the collection of a wide range of information about websites.
* **Efficiency and Expertise: :** Building a similar solution independently would be very time-consuming and require specialized knowledge.
* **Open Source Advantage: :** Publishing this tool as open source will facilitate many studies, making them simpler and allowing researchers and industry professionals to focus on more advanced tasks.
* **Continuous Improvement: :** New techniques will be added successively, ensuring continuous growth in this area.

## Features
- Integration of 20 Different Sources: Reduces the need to maintain multiple integrations.
- Local Data Collection: Supports building and maintaining local phishing databases.
- Data Export: Allows exporting all collected data in a unified JSON format.
- Asynchronous Performance: Uses asyncio for faster, simultaneous data collection.

### Integrations
- BinaryDefence
- BlockListDe
- Botvrij
- C2IntelFeeds
- C2Tracker
- CertPL
- Ellio
- GreenSnow
- MiraiSecurity
- OpenPhish
- PhishTank
- PhishingArmy
- PhishingDatabase
- PhishStats
- Proofpoint
- ThreatView
- TweetFeed
- URLAbuse
- URLHaus
- Valdin

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

## Contributing

For contributing, refer to its [CONTRIBUTING.md](.github/CONTRIBUTING.md) file.
We are a welcoming community... just follow the [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## Maintainers

Project maintainers are:

- Damian Frąszczak
- Edyta Frąszczak

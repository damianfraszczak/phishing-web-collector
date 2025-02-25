# Quick Start Guide for PhishingWebCollector

Web2Vec is a comprehensive library designed to convert websites into vector parameters. It provides ready-to-use implementations of web crawlers using Scrapy, making it accessible for less experienced researchers. This tool is invaluable for website analysis tasks, including SEO, disinformation detection, and phishing identification.

## Installation

Install PhishingWebCollector using pip:

```bash
pip install phishing-web-collector
```
#
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

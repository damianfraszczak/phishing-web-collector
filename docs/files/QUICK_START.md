# Quick Start Guide for PhishingWebCollector

PhishingWebCollector is a comprehensive library designed to convert websites into vector parameters. It provides ready-to-use implementations of web crawlers using Scrapy, making it accessible for less experienced researchers. This tool is invaluable for website analysis tasks, including SEO, disinformation detection, and phishing identification.

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

## Jupyter Notebook Usage
If you would like to test ``PhishingWebCollector`` functionalities without installing it on your machine consider using the preconfigured [Jupyter notebook](docs/files/jupyter/collect_phishing_domains.ipynb). It will show you how to collect phishing domains from all available sources and save them into a CSV file. You can run it in your browser without any installation using [Google Colab](https://colab.research.google.com/github/damianfraszczak/phishing-web-collector/blob/master/docs/files/jupyter/collect_phishing_domains.ipynb).

To check how asynchronous data collection is faster than synchronous one, you can run the [asynchronous benchmark notebook](docs/files/jupyter/sync_vs_async_benchmark.ipynb).

To check how to run feeds directly, you can run the [direct feed invocation notebook](docs/files/jupyter/direct_feed_invocation.ipynb).

To check how to filter feeds, you can run the [filter feeds notebook](docs/files/jupyter/filter_phishing_entries.ipynb).

## Docker usage
If you want to use PhishingWebCollector in a Docker container, please check this [README](docker/README.md) file.

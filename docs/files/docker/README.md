# PhishingWebCollector Docker usage

This sample demonstrates how to use the PhishingWebCollector project in a Docker container.
It will run the [collect_phishing_domains.py](collect_phishing_domains.py) script that will process defined phishing feeds and save them in a CSV file.

1. Install Docker
2. Clone this repository
3. Build the Docker image - [Dockerfile](.Dockerfile)

```bash
docker build -t phishing-web-collector .
```

4. Run the Docker container. It will run the [collect_phishing_domains.py](collect_phishing_domains.py) script that will process defined phishing feeds and save them in a CSV file.


```bash
docker run -it phishing-web-collector
```

# PhishingWebCollector: A Python Library for Phishing Website Collection 

## Overview
`PhishingWebCollector` is a Python library that integrates 20 phishing feeds into one solution and offers a platform for collecting and managing malicious website data.
Suitable for practical cybersecurity applications, like updating local blacklists, and research, such as building phishing detection datasets.
It utilizes the asyncio module for efficient parallel processing and data collection.
Users can gather historical data from free feeds to construct extensive datasets without costly API subscriptions.
Its ease of use, scalability, and support for various data formats enhance the threat detection capabilities of cybersecurity teams and researchers while minimizing technical overhead.


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

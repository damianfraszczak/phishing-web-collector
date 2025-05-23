FROM python:3.10-slim

WORKDIR /app

COPY collect_phishing_domains.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "collect_phishing_domains.py"]

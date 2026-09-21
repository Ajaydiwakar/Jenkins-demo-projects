FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# This is a one-off script, not a web server, so no EXPOSE is needed
CMD ["python", "scraper.py"]

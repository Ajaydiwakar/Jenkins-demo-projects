import requests
from bs4 import BeautifulSoup
import datetime

def run_scraper():
    print(f"[{datetime.datetime.now()}] Starting web scraping task...")
    try:
        # Scraping a safe, public example domain
        response = requests.get("https://example.com")
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No Title Found"
        
        print(f"Successfully scraped example.com!")
        print(f"Page Title: {title}")
        
    except Exception as e:
        print(f"An error occurred during scraping: {e}")

if __name__ == "__main__":
    run_scraper()

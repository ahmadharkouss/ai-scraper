import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#TODO: improve scrapper to dectect links in the page and scrape them
class DataExtractor:
    def __init__(self, use_selenium=False):
        self.use_selenium = use_selenium
        if self.use_selenium:
            self.driver = self.init_selenium_driver()

    def init_selenium_driver(self):
        # Initialize Selenium WebDriver using ChromeDriverManager
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode (no UI)
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)

    def fetch_content(self, url):
        # Use Selenium for dynamic content, requests for static pages
        if self.use_selenium:
            try:
                self.driver.get(url)
                time.sleep(2)  # Wait for the page to fully load
                page_source = self.driver.page_source
                return page_source
            except Exception as e:
                print(f"Error with Selenium for {url}: {e}")
                return None
        else:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise error for bad responses
                return response.text
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")
                return None

    def extract_relevant_data(self, url):
        # Fetch page content (dynamic or static)
        content = self.fetch_content(url)
        if not content:
            return None

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')

        # Extract title, summary, and date
        title = soup.find('h1').get_text() if soup.find('h1') else 'No title found'
        summary = soup.find('meta', attrs={'name': 'description'})
        summary_text = summary['content'] if summary else 'No summary found'
        published_date = soup.find('time')  # Example tag for date extraction
        date_text = published_date['datetime'] if published_date and 'datetime' in published_date.attrs else 'No date found'

        # Extract main text from <p>, <article>, and possibly other tags
        #paragraphs = soup.find_all('p')
        #article_body = " ".join([p.get_text() for p in paragraphs]) if paragraphs else 'No content found'

        # If no <p> tags found, try <div> with class or id commonly used for content
        #if not article_body.strip():
         #   divs = soup.find_all('div', {'class': 'content'})
          #  article_body = " ".join([div.get_text() for div in divs]) if divs else 'No content found'

        paragraphs = soup.find_all('p')
        article_body = " ".join([p.get_text() for p in paragraphs]) if paragraphs else 'No content found'
        
        a_tags = soup.find_all('a')
        article_body = " ".join([a.get_text() for a in a_tags]) if a_tags else 'No content found'

        # Return a structured data dictionary with full text
        return {
            'url': url,
            'title': title,
            'summary': summary_text,
            'date': date_text,
            'content': article_body  # Full article text
        }

    def close_selenium(self):
        if self.use_selenium:
            self.driver.quit()

# Storing and organizing data in a list of dictionaries
class DataStorage:
    def __init__(self):
        self.data = []

    def store_data(self, data):
        if data:
            self.data.append(data)

    def get_all_data(self):
        return self.data
    def output_data_to_txt(self, filename="output.txt"):
        #create a text file and write all data to it
        with open(filename, 'w') as file:
            for entry in self.data:
                #file.write(f"Title: {entry['title']}\n")
                #file.write(f"Summary: {entry['summary']}\n")
               # file.write(f"Date: {entry['date']}\n")
                file.write(f"URL: {entry['url']}\n")
                file.write(f"Content: {entry['content']}\n\n")
                 #file.write(f"Summary: {entry['summary']}\n")
                #file.write(f"Content: {entry['content']}\n\n")

                  
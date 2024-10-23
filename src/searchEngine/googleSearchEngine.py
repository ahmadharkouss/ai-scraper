import requests
import json


"""
This class interfaces with the Google Custom Search API to search for news articles 
related to a specific company, using custom search terms provided in a JSON file. 

Key Features:
- Searches for news articles in French, with an emphasis on recent news.
- Supports queries for both the company name and an optional SIRET number for more 
  specific results.
- Allows customization of search terms via a JSON file, which are combined using 
  `orTerms` to enhance the search query.
- Retrieves up to three relevant search results per query, focusing on French news sources.

Attributes:
- `api_key`: The API key required to authenticate the requests to the Google Custom Search API.
- `search_engine_id`: The unique identifier for the custom search engine.
- `search_terms_dict`: A dictionary of search terms loaded from a JSON file, which helps to 
  refine the search query.

Methods:
- `generate_orTerms_from_dict()`: Converts search terms stored in the dictionary into a single 
  string of OR terms to improve the search query.
- `search(companyName, SiretNumber)`: Executes the search query using the Google Custom Search API, 
  incorporating the company name, SIRET number (if provided), and custom search terms. Returns a 
  list of URLs corresponding to the search results.

API Documentation:
- Refer to the official Google Custom Search API documentation for additional details: 
  https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
"""
class GoogleSearchEngine:
    def __init__(self, api_key, search_engine_id, json_file):
        self.api_key = api_key
        self.search_engine_id = search_engine_id
        # Load search terms from a JSON file
        with open(json_file, 'r', encoding='utf-8') as file:
            self.search_terms_dict = json.load(file)


    # Function to convert dictionary values into a single orTerms string
    def generate_orTerms_from_dict(self):
        all_terms = []
        for _, terms in self.search_terms_dict.items():
            all_terms.extend(terms)
        return " ".join(all_terms)  # Join all terms into a single string for the query

    def search(self,companyName, SiretNumber):
        search_url = f"https://www.googleapis.com/customsearch/v1"
        params = {
            'q': f"{companyName} actualités",
            'cx': self.search_engine_id,
            'key': self.api_key,
            'num': 3,
            'cr': 'countryFR',
            'gl': 'fr',
            'hl': 'fr',
            'hq': f"{companyName} (SIRET: {SiretNumber})" if SiretNumber else companyName,
            'orTerms': self.generate_orTerms_from_dict(),
            'lr': 'lang_fr',
            'exactTerms': companyName,
            'safe': 'off',
            'sort': 'date',
            #'siteSearchFilter': 'e', 
            #'siteSearch': 'https://fr.linkedin.com/',
        }
        response = requests.get(search_url, params=params)
        search_results = response.json()
        urls = []
        if 'items' in search_results:
            for item in search_results['items']:
                urls.append(item['link'])
        return urls



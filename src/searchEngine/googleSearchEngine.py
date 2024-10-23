import requests
import json


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

    #doc: https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
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



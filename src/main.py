from searchEngine.googleSearchEngine import GoogleSearchEngine
from scraper.scraper import DataExtractor, DataStorage
from scraper.preprocessor import Summarizer
import os


#For Now, Api keys are public and can be used by anyone
API_KEY = 'AIzaSyBBklNgC49Xw8fp5Wtw8LImqEM5PBYYTgY'
SEARCH_ENGINE_ID = 'f18cbde5698aa4a70'



if __name__ == "__main__":

    # Get the absolute path to the directory where your script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the search_terms.json file
    search_terms_path = os.path.join(base_dir, 'searchEngine', 'search_terms.json')

    # Initialize GoogleSearchEngine using the absolute path
    googleSearchEngine = GoogleSearchEngine(API_KEY, SEARCH_ENGINE_ID, search_terms_path)

    urls = googleSearchEngine.search(
    SiretNumber=None,
    companyName="Thales")

    # Initialize data extractor with Selenium
    data_extractor = DataExtractor(use_selenium=True)
    storage = DataStorage()

    # Extract and store data for each URL
    for url in urls:
        relevant_data = data_extractor.extract_relevant_data(url)
        storage.store_data(relevant_data)

    summarizer = Summarizer()

    # Print stored data
    all_data = storage.get_all_data()
    all_text_content =""
    for entry in all_data:
        if entry:
            text_content = summarizer.preprocess_data(entry['content'], "Thales")
            entry['content'] = text_content
            #check if content is not empty and do not contain only one line
            if text_content and len(text_content.splitlines()) > 1:
                all_text_content += text_content

  
    #Print Summary    
    summary = summarizer.summarize_text(all_text_content)
    print(summary)
    # Close the Selenium driver when done
    data_extractor.close_selenium()
    #Output all content data to a text file
    storage.output_data_to_txt()

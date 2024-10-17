from searchEngine.googleSearchEngine import GoogleSearchEngine
from scraper.scraper import DataExtractor, DataStorage
from scraper.preprocessor import Summarizer



API_KEY = 'AIzaSyBBklNgC49Xw8fp5Wtw8LImqEM5PBYYTgY'
SEARCH_ENGINE_ID = 'f18cbde5698aa4a70'



if __name__ == "__main__":

    googleSearchEngine = GoogleSearchEngine(API_KEY, SEARCH_ENGINE_ID, 'searchEngine/search_terms.json')

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
            #print(text_content)
            #check if content is not empty and do not contain only one line
            if text_content and len(text_content.splitlines()) > 1:
                all_text_content += text_content


    print(all_text_content)       
    #Print Summary    
    summary = summarizer.summarize_text(all_text_content)
    print(summary)
    # Close the Selenium driver when done
    data_extractor.close_selenium()

    #Output all content data to a text file
    storage.output_data_to_txt()

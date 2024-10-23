import os
from dotenv import load_dotenv


from searchEngine.googleSearchEngine import GoogleSearchEngine
from scraper.graphScraper import GraphScraper
from classifier.newsLabelClassifier import NewsLabelClassifier


# Load the environment variables
load_dotenv()
CUSTOM_SEARCH_API_KEY = os.getenv("CUSTOM_SEARCH_API_KEY")  
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
OPENAPI_KEY = os.getenv("OPENAPI_KEY")

# Company information
COMPANY_NAME="Groupe ROUTHIAU"
SIRET=31261392000049

if __name__ == "__main__":

    # Get the absolute path to the directory where your script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the search_terms.json file
    search_terms_path = os.path.join(base_dir, 'searchEngine', 'search_terms.json')

    #Construct the absolute path to the labels.json file
    labels_file_path = os.path.join(base_dir, 'classifier', 'labels.json')

    # Initialize GoogleSearchEngine using the absolute path
    googleSearchEngine = GoogleSearchEngine(CUSTOM_SEARCH_API_KEY, SEARCH_ENGINE_ID, search_terms_path)

    #Get urls
    urls = googleSearchEngine.search(
    SiretNumber=SIRET,
    companyName=COMPANY_NAME)
    print("Found urls:")
    print(urls)
    print()

    #Initialize GraphScraper
    GraphScraper = GraphScraper(OPENAPI_KEY, COMPANY_NAME, urls)
    #Get news summary
    results= GraphScraper.run()
    print("Summary with urls sources:")
    print(results)
    print()

    #Initialize NewsLabelClassifier
    newsLabelClassifier = NewsLabelClassifier(labels_file_path, results['summary'])
    #Get label
    label = newsLabelClassifier.run()
    print("Label:")
    print(label)
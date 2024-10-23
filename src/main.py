import os
from dotenv import load_dotenv


from searchEngine.googleSearchEngine import GoogleSearchEngine
from scraper.graphScraper import GraphScraper
from classifier.newsLabelClassifier import NewsLabelClassifier

load_dotenv()

#For Now, Api keys are public and can be used by anyone
API_KEY = 'AIzaSyBBklNgC49Xw8fp5Wtw8LImqEM5PBYYTgY'
SEARCH_ENGINE_ID = 'f18cbde5698aa4a70'
#Replace by env variables
openai_key = "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"
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
    googleSearchEngine = GoogleSearchEngine(API_KEY, SEARCH_ENGINE_ID, search_terms_path)

    #Get urls
    urls = googleSearchEngine.search(
    SiretNumber=SIRET,
    companyName=COMPANY_NAME)
    print("Found urls:")
    print(urls)
    print()

    #Initialize GraphScraper
    GraphScraper = GraphScraper(openai_key, COMPANY_NAME, urls)
    #Get news summary
    results= GraphScraper.run()
    print("Summary with urls sources:")
    print(results)

    #Initialize NewsLabelClassifier
    newsLabelClassifier = NewsLabelClassifier(labels_file_path, results['summary'])
    #Get label
    label = newsLabelClassifier.run()
    print("Label:")
    print(label)



   

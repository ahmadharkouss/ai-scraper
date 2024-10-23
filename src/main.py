import os
from dotenv import load_dotenv


from searchEngine.googleSearchEngine import GoogleSearchEngine
from scrapegraphai.graphs import SmartScraperGraph, SmartScraperMultiGraph
from scrapegraphai.utils import prettify_exec_info

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

    # Initialize GoogleSearchEngine using the absolute path
    googleSearchEngine = GoogleSearchEngine(API_KEY, SEARCH_ENGINE_ID, search_terms_path)

    urls = googleSearchEngine.search(
    SiretNumber=SIRET,
    companyName=COMPANY_NAME)
    print(urls)

    graph_config = {
           "llm": {
              "api_key": openai_key,
              "model": "openai/gpt-4o-mini",
           },
        }

    # ************************************************
    # Create the SmartScraperGraph instance and run it
    # ************************************************
    smart_scraper_graph = SmartScraperMultiGraph(
       prompt=f"Give me the news summary in French for {COMPANY_NAME} in one block",
       # also accepts a string with the already downloaded HTML code
       source=urls,
       config=graph_config
    )
    
    result = smart_scraper_graph.run()
    print(result)


   

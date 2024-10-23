import os
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph, SmartScraperMultiGraph
from scrapegraphai.utils import prettify_exec_info

load_dotenv()

#Replace by env variables
openai_key = "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"

graph_config = {
   "llm": {
      "api_key": openai_key,
      "model": "openai/gpt-4o-mini",
   },
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************
sources= ["https://www.zonebourse.com/cours/action/THALES-4715/actualite/", "https://www.thalesgroup.com/fr"
          ,"https://www.zonebourse.com/cours/action/THALES-4715/"]
smart_scraper_graph = SmartScraperMultiGraph(
   prompt="Give me the news summary in French.",
   # also accepts a string with the already downloaded HTML code
   source=sources,
   config=graph_config
)

result = smart_scraper_graph.run()
print(result)


#modfy it to scrap max 3 urls 
#next use sentiment analysis to get the sentiment of the news
#add



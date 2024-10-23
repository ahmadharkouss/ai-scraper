from scrapegraphai.graphs import SmartScraperGraph, SmartScraperMultiGraph
from scrapegraphai.utils import prettify_exec_info

"""
This class is responsible for retrieving and summarizing news articles for a given company 
in French. It uses the `SmartScraperMultiGraph` class from the `scrapegraphai` library to 
perform web scraping and summarize relevant information about the company.

Key Features:
- Utilizes a multi-source scraping approach to gather news from multiple websites.
- Provides a concise news summary in French related to the specified company.
- Supports easy customization of scraping prompts and configuration settings.

For more details, refer to the official documentation at:
https://scrapegraph-ai.readthedocs.io/en/latest/modules/modules.html
"""
class GraphScraper:
    def __init__(self, openai_key, company_name, urls):
        self.openai_key = openai_key
        self.company_name = company_name
        self.urls=urls

    def run(self):
        
        graph_config = {
            "llm": {
                "api_key": self.openai_key,
                "model": "openai/gpt-4o-mini",
            },
        }

        smart_scraper_graph = SmartScraperMultiGraph(
            prompt=f"Give me the news summary in French for {self.company_name} in one block",
            source=self.urls,
            config=graph_config
        )

        summary = smart_scraper_graph.run()
        return summary
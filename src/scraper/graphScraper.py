from scrapegraphai.graphs import SmartScraperGraph, SmartScraperMultiGraph
from scrapegraphai.utils import prettify_exec_info


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
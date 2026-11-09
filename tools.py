import time

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper, DuckDuckGoSearchAPIWrapper
from langchain_core.tools import Tool
from datetime import datetime

# Create a function to save the research report to a text file
def save_to_txt(data: str, filename: str = "research_report.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"Research Report - {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data saved to {filename}"

# Tool for saving the research report to a text file
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Save the research report to a text file with a timestamp.",
)

# Wikipedia tool for querying information
# The default region "wt-wt" makes ddgs query a Wikipedia site that doesn't exist, so set one.
search = DuckDuckGoSearchAPIWrapper(region="us-en")

# The free search and Wikipedia APIs sometimes fail or come back empty, so retry a few
# times and return a message instead of raising, which would stop the whole agent.
def run_with_retries(func, query: str, failure_message: str, attempts: int = 3) -> str:
    for attempt in range(attempts):
        try:
            return func(query)
        except Exception:
            if attempt < attempts - 1:
                time.sleep(2)
    return failure_message

search_tool = Tool(
    name="search",
    func=lambda query: run_with_retries(
        search.run, query, "Web search failed. Try the wikipedia tool instead."
    ),
    description="Search the web for information",
)

# Wikipedia API wrapper: This tool retrieves information from Wikipedia
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)

# Wikipedia tool for querying information using the API wrapper
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
wiki_tool = Tool(
    name=wiki.name,
    func=lambda query: run_with_retries(
        wiki.run, query, "Wikipedia lookup failed. Try the search tool instead."
    ),
    description=wiki.description,
)
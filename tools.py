from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
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
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)

# Wikipedia API wrapper: This tool retrieves information from Wikipedia
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)

# Wikipedia tool for querying information using the API wrapper
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
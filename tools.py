from langchain_community.tools import DuckDuckGoSearchResults , WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper 
from langchain.tools import Tool    
from datetime import datetime



# TOOL 1 : DuckDuckGo Search Tool
search=DuckDuckGoSearchResults()
search_tool=Tool(
    name="duckduckgo_search",
    func=search.run,
    description="search the web for recent information on a topic"
)   


# TOOL 2 : Wikipedia Tool
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool =  WikipediaQueryRun(api_wrapper=api_wrapper)


# TOOL 3 : Save to text file tool
def save_to_txt(query: str):
    """
    Save research results to a text file.
    Args:
        query: The complete research summary to save
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "research_output.txt"
    
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{query}\n\n" + "="*50 + "\n\n"

    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(formatted_text)
        return f"Data successfully saved to {filename}"
    except Exception as e:
        return f"Error saving file: {str(e)}"

# wrapping the function as a Tool
save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Use this tool to save research results to a text file. Pass the complete research summary as a single string parameter.",
)
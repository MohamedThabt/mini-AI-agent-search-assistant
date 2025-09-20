# main agent logic
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent , AgentExecutor
from tools import search_tool , wiki_tool , save_tool


load_dotenv()  # Load environment variables from .env file


# Define all fields that you want from LLM call 
class ResearchResponse(BaseModel):
    topic: str
    answer: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY")
)  


# Create a Pydantic output parser based on the ResearchResponse model
parser = PydanticOutputParser(pydantic_object=ResearchResponse) 

prompt_template = ChatPromptTemplate.from_messages([
    ("system", 
        """
        You are a helpful research assistant. You will be given a topic to research.
        
        CRITICAL: You MUST use the available tools to gather information. Do NOT generate responses from your training data.
        
        Available tools:
        - duckduckgo_search: Search the web for recent information
        - wikipedia: Get information from Wikipedia  
        - save_text_to_file: Save research results to a text file
        
        Process:
        1. Use duckduckgo_search to search for the topic
        2. Use wikipedia for additional context if needed
        3. If user requests saving to file, use save_text_to_file tool
        4. After using tools, provide your final response
        
        Always call the tools first, then provide your response.
        """),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])


tools=[search_tool, wiki_tool , save_tool ]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt_template,
    tools=tools,
)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, 
    tools=tools, 
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5
) 

query = input("What can i help you research? ")
raw_response = agent_executor.invoke({"input": query})

# Print the response from the agent
print(f"\nResearch Results:")
print(raw_response['output'])
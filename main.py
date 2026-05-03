from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from tavily import TavilyClient
from typing import List
from pydantic import BaseModel, Field

import os
os.system('cls')
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search(query: str) -> str:
    """
    Tool that searches the internet
    Args:
        query: The search to query for
    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    return tavily_client.search(query)


llm = ChatOpenAI()
tools = [TavilySearch(), search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from sourav-ai-agents!")
    result = agent.invoke({'messages': [HumanMessage(content="Job openings for langchain engineers in Kolkata?")]})
    print(f"🤖 Agent response: {result['messages'][-1].content}")

if __name__ == "__main__":
    main()
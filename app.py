import os
from dotenv import load_dotenv
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model
# from langchain_core.memory import SimpleMemory


# store = SimpleMemory()

load_dotenv()

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')



tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def internet_search(
    query : str,
    max_results : int = 5,
    topic : Literal["general", "news", "finance"] = "general",
    include_raw_content : bool = False,
):

    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        topic=topic,
        include_raw_content=include_raw_content
    )

research_instructions =  """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
When users tell you their preferences, save them to /memories/user_preferences.txt so you remember them in future conversations.
"""

model = init_chat_model(
    "deepseek-chat",
    model_provider="deepseek",
    api_key=DEEPSEEK_API_KEY,
)

agent = create_deep_agent(
    model=model,
    # store=store,
    # use_longterm_memory=True,
    tools=[internet_search],
    system_prompt=research_instructions
)

result = agent.invoke({"messages": [{"role": "user", "content": "Research the rise of electric vehicle adoption in Africa, identify the top 3 countries leading the transition, and explain the main policy, infrastructure, and investment factors behind their success"}]})


print(result["messages"][-1].content)
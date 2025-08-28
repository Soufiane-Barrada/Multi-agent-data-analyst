from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from ..tools import wikipedia_tool, stock_data_tool
from ..config.settings import settings


def create_research_agent(llm = None):
    """
    Args:
        llm: The language model to use.

    """
    if llm is None:
        llm = ChatOpenAI(model=settings.MODEL_NAME)
    
    research_agent = create_react_agent(
        llm,
        tools=[wikipedia_tool, stock_data_tool],
        prompt=(
            "You are a research agent.\n\n"
            "INSTRUCTIONS:\n"
            "- Assist ONLY with research-related tasks, including looking-up factual information and stock data. DO NOT write any code.\n"
            "- After you're done with your tasks, respond to the supervisor directly\n"
            "- Respond ONLY with the results of your work, do NOT include ANY other text."
        ),
        name=settings.RESEARCH_AGENT_NAME
    )
    
    return research_agent 
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from ..tools import python_repl_tool
from ..config.settings import settings


def create_analyst_agent(llm= None):
    """
    Args:
        llm: The language model to use. If None, creates a new ChatOpenAI instance.

    """
    if llm is None:
        llm = ChatOpenAI(model=settings.MODEL_NAME)
    
    analyst_agent = create_react_agent(
        llm,
        [python_repl_tool],
        prompt=(
            "You are an agent that can run arbitrary Python code.\n\n"
            "INSTRUCTIONS:\n"
            "- Assist ONLY with tasks that require running code to produce an output.\n"
            "- After you're done with your tasks, respond to the supervisor directly\n"
            "- Respond ONLY with the results of your work, do NOT include ANY other text."
        ),
        name=settings.ANALYST_AGENT_NAME
    )
    
    return analyst_agent 
from langchain_openai import ChatOpenAI
from langgraph_supervisor import create_supervisor
from langgraph.checkpoint.memory import InMemorySaver

from .agents import create_research_agent, create_analyst_agent
from .config.settings import settings


class MultiAgentSupervisor:
    
    def __init__(self, llm=None):
        """
        Args:
            llm: The language model to use. 
        """
        if llm is None:
            llm = ChatOpenAI(model=settings.MODEL_NAME)
        
        self.llm = llm
        self.checkpointer = InMemorySaver()
        
        # Create agents
        self.research_agent = create_research_agent(llm)
        self.analyst_agent = create_analyst_agent(llm)
        
        # Create supervisor
        self.supervisor = create_supervisor(
            model=llm,
            agents=[self.analyst_agent, self.research_agent],
            prompt=("You are a supervisor managing two agents:\n"
                "- a research agent. Assign research and data collection tasks to this agent\n"
                "- an analyst agent. Assign the creation of visualizations via code to this agent\n"
                "Assign work to one agent at a time, do not call agents in parallel.\n"
                "Do not do any work yourself."),
            add_handoff_back_messages=True,
            output_mode="full_history",
        ).compile(checkpointer=self.checkpointer)
    
    def get_config(self):
        return {
            "configurable": {
                "thread_id": settings.THREAD_ID,
                "user_id": settings.USER_ID
            }
        }


    # a generator functions that yields chunks of the output.
    def process_query(self, query: str):
        """Process a user query through the multi-agent system.
        Args:
            query: The user's query string.
        """
        config = self.get_config()
        
        for chunk in self.supervisor.stream(
            {"messages": [{"role": "user", "content": query}]}, 
            config
        ):
            yield chunk
    


    def visualize_graph(self):
        """Return the supervisor graph for visualization."""
        return self.supervisor 
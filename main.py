import argparse
import sys
from typing import Optional

from src.supervisor import MultiAgentSupervisor
from src.utils.display import pretty_print_messages
from src.config.settings import settings


def run_single_query(query: str):

    print(f"Processing: {query}")
    print("-" * 50)
    
    supervisor = MultiAgentSupervisor()
    try:
        for chunk in supervisor.process_query(query):
            pretty_print_messages(chunk)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)



def main():

    parser = argparse.ArgumentParser(
        description="Multi-Agent Data Analyst",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        Example:
        python main.py --query "What is Tesla's stock performance last month?"
        """
    )
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="Single query to process"
    ) 
    
    args = parser.parse_args()
    run_single_query(args.query)



if __name__ == "__main__":
    main() 
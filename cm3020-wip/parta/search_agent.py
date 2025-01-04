import re
import time
from typing import Dict, List
from functools import lru_cache
from langchain_anthropic import ChatAnthropic
import ratelimit
from langchain import LLMChain, PromptTemplate
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent, AgentOutputParser
from langchain.prompts import BaseChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage, AgentAction, AgentFinish
from langchain.tools import DuckDuckGoSearchRun
from langchain.chat_models import ChatOpenAI
from langgraph.graph import StateGraph, END

# Configuration
WEBSITES = ["scholar.google.com","arxiv.org", "jstor.org", "researchgate.net", "ieeexplore.ieee.org"]
RATE_LIMIT = 1  # requests per second
CACHE_SIZE = 100

class SearchError(Exception):
    """Custom exception for search-related errors"""
    pass

@lru_cache(maxsize=CACHE_SIZE)
def cached_search(query: str) -> str:
    """Cached version of the search function"""
    return _perform_search(query)

@ratelimit.limits(calls=RATE_LIMIT, period=1)
def _perform_search(query: str) -> str:
    """Rate-limited search function"""
    try:
        search = DuckDuckGoSearchRun()
        site_query = " OR ".join([f"site:{site}" for site in WEBSITES])
        full_query = f"({query}) ({site_query})"
        return search.run(full_query)
    except Exception as e:
        raise SearchError(f"Search failed: {str(e)}")

def custom_search(query: str) -> str:
    """Main search function with error handling"""
    try:
        return cached_search(query)
    except ratelimit.RateLimitException:
        time.sleep(1)  # Wait for rate limit to reset
        return cached_search(query)
    except SearchError as e:
        return f"Error during search: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# Create search tool
search_tool = Tool(
    name="Custom Search",
    func=custom_search,
    description="Searches the given website for the given query"
)

class CustomOutputParser(AgentOutputParser):
    def parse(self, llm_output: str) -> AgentAction | AgentFinish:
        """Parse LLM output into agent action or finish"""
        if "Final Answer:" in llm_output:
            return AgentFinish(
                return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                log=llm_output,
            )
        
        action_match = re.search(r"Action: (.*?)[\n]", llm_output)
        #input_match = re.search(r"Action Input: (.*?)[\n]", llm_output)
        input_match = re.search(r"Action Input:?\s*(.*?)(?:\n|$)", llm_output, re.DOTALL)
        
        if not action_match or not input_match:
            raise ValueError(f"Could not parse LLM output: {llm_output}")
            
        action = action_match.group(1).strip()
        action_input = input_match.group(1).strip()
        
        return AgentAction(tool=action, tool_input=action_input, log=llm_output)

class CustomPromptTemplate(BaseChatPromptTemplate):
    template: str
    tools: List[Tool]

    def format_messages(self, **kwargs) -> List[HumanMessage]:
        intermediate_steps = kwargs.pop("intermediate_steps")
        thoughts = ""
        for action, observation in intermediate_steps:
            thoughts += f"Action: {action.tool}\nAction Input: {action.tool_input}\nObservation: {observation}\nThought: I now know the result of the action.\n"
        
        kwargs["agent_scratchpad"] = thoughts
        kwargs["tools"] = "\n".join([f"{tool.name}: {tool.description}" for tool in self.tools])
        kwargs["tool_names"] = ", ".join([tool.name for tool in self.tools])
        
        formatted = self.template.format(**kwargs)
        return [HumanMessage(content=formatted)]

def format_results(query: str, results: str) -> Dict:
    """Format the search results"""
    return {
        "query": query,
        "websites_searched": WEBSITES,
        "results": results,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    # Set up the agent
    template = """Answer the following questions as best you can using the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Question: {input}
    {agent_scratchpad}"""

    prompt = CustomPromptTemplate(
        template=template,
        tools=[search_tool],
        input_variables=["input", "intermediate_steps"]
    )

    # llm = ChatOpenAI(temperature=0)
    llm = ChatAnthropic(model_name="claude-3-5-sonnet-latest", temperature=0)
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    output_parser = CustomOutputParser()
    
    agent = LLMSingleActionAgent(
        llm_chain=llm_chain,
        output_parser=output_parser,
        stop=["\nObservation:"],
        allowed_tools=[search_tool.name]
    )

    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=[search_tool],
        verbose=True
    )

    # Execute search
    search_queries = [
        "AI game playing motivation",
        "purpose of game AI",
        "game AI benefits", 
        "game playing ai"
    ]

    results = []
    for query in search_queries:
        try:
            result = agent_executor.run(query)
            formatted_result = format_results(query, result)
            results.append(formatted_result)
        except Exception as e:
            print(f"Error processing query '{query}': {str(e)}")
            results.append(format_results(query, f"Error: {str(e)}"))

    return results

if __name__ == "__main__":
    results = main()
    
    # Print results in a formatted way
    for result in results:
        print("\n" + "="*50)
        print(f"Query: {result['query']}")
        print(f"Websites searched: {', '.join(result['websites_searched'])}")
        print(f"Timestamp: {result['timestamp']}")
        print("\nResults:")
        print(result['results'])
        print("="*50)
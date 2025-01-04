from typing import List, Optional, Literal
from typing_extensions import TypedDict

from langchain_core.messages import HumanMessage

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.types import Command
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.language_models.chat_models import BaseChatModel

from IPython.display import Image, display


from generic_utils import load_text
from team_builder_utils import scrape_webpages

llm = ChatOpenAI(model="gpt-4o")
tavily_tool = TavilySearchResults(max_results=5)
        

search_agent = create_react_agent(llm, tools=[tavily_tool])


def search_node(state: MessagesState) -> Command[Literal["supervisor"]]:
    result = search_agent.invoke(state)
    return Command(
        update={
            "messages": [
                HumanMessage(content=result["messages"][-1].content, name="search")
            ]
        },
        # We want our workers to ALWAYS "report back" to the supervisor when done
        goto="supervisor",
    )


web_scraper_agent = create_react_agent(llm, tools=[scrape_webpages])


def web_scraper_node(state: MessagesState) -> Command[Literal["supervisor"]]:
    result = web_scraper_agent.invoke(state)
    return Command(
        update={
            "messages": [
                HumanMessage(content=result["messages"][-1].content, name="web_scraper")
            ]
        },
        # We want our workers to ALWAYS "report back" to the supervisor when done
        goto="supervisor",
    )




class TeamBuilder:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o")
        self.tavily_tool = TavilySearchResults(max_results=5)
        self.search_agent = create_react_agent(self.llm, tools=[self.tavily_tool])
        self.web_scraper_agent = create_react_agent(self.llm, tools=[scrape_webpages])

        
        self.supervisor_node = self.make_supervisor_node(self.llm, ["search", "web_scraper"])
        self.team_builder = StateGraph(MessagesState)
        self.team_builder.add_node("supervisor", self.supervisor_node)
        self.team_builder.add_node("search", search_node)
        self.team_builder.add_node("web_scraper", web_scraper_node)
        self.team_builder.add_edge(START, "supervisor")
        self.graph = self.team_builder.compile()
        display(Image(self.graph.get_graph().draw_mermaid_png()))

    def search_node(self, state: MessagesState) -> Command[Literal["supervisor"]]:
        result = self.search_agent.invoke(state)
        return Command(
            update={
                "messages": [
                    HumanMessage(content=result["messages"][-1].content, name="search")
                ]
            },
            # We want our workers to ALWAYS "report back" to the supervisor when done
            goto="supervisor",
        )

    def web_scraper_node(self, state: MessagesState) -> Command[Literal["supervisor"]]:
        result = self.web_scraper_agent.invoke(state)
        return Command(
            update={
                "messages": [
                    HumanMessage(content=result["messages"][-1].content, name="web_scraper")
                ]
            },
            # We want our workers to ALWAYS "report back" to the supervisor when done
            goto="supervisor",
        )

    def make_supervisor_node(self, llm: BaseChatModel, members: list[str]) -> str:
        options = ["FINISH"] + members
        system_prompt = (
            "You are a supervisor tasked with managing a conversation between the"
            f" following workers: {members}. Given the following user request,"
            " respond with the worker to act next. Each worker will perform a"
            " task and respond with their results and status. When finished,"
            " respond with FINISH."
        )

        class Router(TypedDict):
            """Worker to route to next. If no workers needed, route to FINISH."""

            next: Literal[*options]

        def supervisor_node(state: MessagesState) -> Command[Literal[*members, "__end__"]]:
            """An LLM-based router."""
            messages = [
                {"role": "system", "content": system_prompt},
            ] + state["messages"]
            response = llm.with_structured_output(Router).invoke(messages)
            goto = response["next"]
            if goto == "FINISH":
                goto = END

            return Command(goto=goto)

        return supervisor_node

    def execute(self, assigment_path:str):
        self.assigment = load_text(assigment_path)

        for s in self.graph.stream(
            {
                "messages": [
                    ("user", "Research AI agents and write a brief report about them.")
                ],
            },
            {"recursion_limit": 150},
        ):
            print(s)
            print("---")




if __name__ == "__main__":
    supervisor = TeamBuilder()
    supervisor.execute("parta.md")

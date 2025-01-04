from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph, MessagesState, START, END

from parta_utils import tavily_tool, make_supervisor_node, search_node, web_scraper_node, python_repl_tool, note_taking_node, chart_generating_node
from parta_utils import llm, scrape_webpages, write_document, edit_document, read_document, create_outline, doc_writing_node, call_research_team, call_paper_writing_team
from generic_utils import load_text


class teams_supervisor:
    def __init__(self):
        self.search_agent = create_react_agent(llm, tools=[tavily_tool])
        self.web_scraper_agent = create_react_agent(llm, tools=[scrape_webpages])

        self.research_supervisor_node = make_supervisor_node(llm, ["search", "web_scraper"])

        self.research_builder = StateGraph(MessagesState)
        self.research_builder.add_node("supervisor", self.research_supervisor_node)
        self.research_builder.add_node("search", search_node)
        self.research_builder.add_node("web_scraper", web_scraper_node)
        self.research_builder.add_edge(START, "supervisor")
        self.research_graph = self.research_builder.compile()
        display(Image(self.research_graph.get_graph().draw_mermaid_png()))

        self.doc_writer_agent = create_react_agent(
            llm,
            tools=[write_document, edit_document, read_document],
            state_modifier=(
                "You can read, write and edit documents based on note-taker's outlines. "
                "Don't ask follow-up questions."
            ),
        )

        self.note_taking_agent = create_react_agent(
            llm,
            tools=[create_outline, read_document],
            state_modifier=(
                "You can read documents and create outlines for the document writer. "
                "Don't ask follow-up questions."
            ),
        )

        self.chart_generating_agent = create_react_agent(
            llm, tools=[read_document, python_repl_tool]
        )

        self.doc_writing_supervisor_node = make_supervisor_node(
            llm, ["doc_writer", "note_taker", "chart_generator"]
        )

        # Create the graph here
        self.paper_writing_builder = StateGraph(MessagesState)
        self.paper_writing_builder.add_node("supervisor", self.doc_writing_supervisor_node)
        self.paper_writing_builder.add_node("doc_writer", doc_writing_node)
        self.paper_writing_builder.add_node("note_taker", note_taking_node)
        self.paper_writing_builder.add_node("chart_generator", chart_generating_node)

        self.paper_writing_builder.add_edge(START, "supervisor")
        self.paper_writing_graph = self.paper_writing_builder.compile()

        self.teams_supervisor_node = make_supervisor_node(llm, ["research_team", "writing_team"])

        # Define the graph.
        self.super_builder = StateGraph(MessagesState)
        self.super_builder.add_node("supervisor", self.teams_supervisor_node)
        self.super_builder.add_node("research_team", call_research_team)
        self.super_builder.add_node("writing_team", call_paper_writing_team)

        self.super_builder.add_edge(START, "supervisor")
        self.super_graph = self.super_builder.compile()

        from IPython.display import Image, display

        display(Image(self.super_graph.get_graph().draw_mermaid_png()))
    
    def execute(self, assigment_path:str):
        self.assigment = load_text(assigment_path)

        for s in self.super_graph.stream(
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
    supervisor = teams_supervisor()
    supervisor.execute("assignment.txt")

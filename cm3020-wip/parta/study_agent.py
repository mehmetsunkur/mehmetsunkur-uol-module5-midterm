"""Study Agent Module.

This module implements an agent that can study and learn from an environment.
It provides the StudyAgent class which handles the interaction between
the agent and its environment.

Typical usage example:
    agent = StudyAgent(environment)
    agent.study()
"""

import logging

from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

looger = logging.getLogger(__name__)


class StudyAgent:
    """Agent that studies and interacts with the environment.

    This class implements an agent that can interact with a given environment
    to learn and make decisions.

    Args:
      environment: The environment the agent will interact with
    """

    def __init__(self, assignment_text_path):
        self.assignment_text_path = assignment_text_path
        with open(assignment_text_path, "r", encoding="utf-8") as file:
            assignment = file.read()
        self.assignment = assignment
        self.memory = MemorySaver()
        self.model = ChatAnthropic(model_name="claude-3-sonnet-20240229")
        self.search = TavilySearchResults(max_results=2)
        self.tools = [self.search]
        self.agent_executor = create_react_agent(
            self.model, self.tools, checkpointer=self.memory
        )

    def run(self):
        """
        Executes the study agent's main loop.
        The study agent interacts with the environment and learns from these
        interactions.
        It should also be capable of predicting the next state given the
         current state and action.
        This method should be implemented to define the specific behavior
        of the study agent.
        """
        looger.info("StudyAgent.run() called")
        # Use the agent
        config = {"configurable": {"thread_id": "abc123"}, "context": self.assignment}
        # ask model to summarize the assignment
        # Define prompt
        # prompt = ChatPromptTemplate.from_messages(
        #     [("system", "Write a concise summary of the following:\\n\\n{context}")]
        # )

        prompt = ChatPromptTemplate.from_messages(
            [("system", "Write a concise summary of the following:\\n\\n{context}")]
        )

        # Instantiate chain
        # chain = create_stuff_documents_chain(llm, prompt)

        # Invoke chain
        # result = chain.invoke({"context": docs})
        # print(result)
        for chunk in self.agent_executor.stream(prompt, config):
            print(chunk)
            print("----")

        for chunk in self.agent_executor.stream(
            {"messages": [HumanMessage(content="hi im bob! and i live in sf")]}, config
        ):
            print(chunk)
            print("----")

        for chunk in self.agent_executor.stream(
            {"messages": [HumanMessage(content="whats the weather where I live?")]},
            config,
        ):
            print(chunk)
            print("----")


# if __name__ == "__main__":
#  load text from file


StudyAgent("parta/parta.md").run()

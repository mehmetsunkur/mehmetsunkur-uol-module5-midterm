from langchain import hub
from langchain.agents import AgentExecutor, create_self_ask_with_search_agent
from langchain_community.chat_models import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults

prompt = hub.pull("hwchase17/self-ask-with-search")
model = ChatAnthropic(model="claude-3-haiku-20240307")
tools = [...]  # Should just be one tool with name `Intermediate Answer`
search = TavilySearchResults(max_results=2)
tools = [search]

agent = create_self_ask_with_search_agent(model, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

agent_executor.invoke({"input": "hi"})

from langchain.agents import create_react_agent, AgentExecutor
from langchain.agents.format_scratchpad import format_log_to_str
from langchain_anthropic import ChatAnthropic
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document


def create_text_summarization_agent():
    # Initialize the LLM
    llm = ChatAnthropic(model_name="claude-3-sonnet-20240229")

    # Create a tool for text summarization
    def summarize_text(text: str) -> str:
        # Split text into chunks if it's too long
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200,
        )

        # Create document object
        docs = [Document(page_content=text)]

        if len(text) > 2000:
            docs = text_splitter.split_documents(docs)

        # Initialize the summarization chain
        chain = load_summarize_chain(llm=llm, chain_type="map_reduce", verbose=True)

        return chain.run(docs)

    tools = [
        Tool(
            name="Summarizer",
            func=summarize_text,
            description="Useful for summarizing text. Input should be the text you want to summarize.",
        )
    ]

    # Create the prompt template
    template = """Answer the following questions as best you can. You have access to the following tools:
    
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

    Begin!

    Question: {input}
    Thought:{agent_scratchpad}"""

    prompt = PromptTemplate.from_template(template)

    # Create memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Create the agent
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True,
    )

    return agent_executor


# Example usage
def main():
    # Create the agent
    agent = create_text_summarization_agent()

    # Example text to summarize
    text_to_summarize = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, 
    as opposed to natural intelligence displayed by animals and humans. 
    AI research has been defined as the field of study of intelligent agents, 
    which refers to any system that perceives its environment and takes actions 
    that maximize its chance of achieving its goals. The term "artificial intelligence" 
    had previously been used to describe machines that mimic and display human cognitive 
    skills that are associated with the human mind, such as learning and problem-solving.
    """

    # Run the agent
    prompt = ChatPromptTemplate.from_messages(
        [("system", "Write a concise summary of the following:\\n\\n{context}")]
    )
    config = {"configurable": {"thread_id": "abc123"}}
    for chunk in agent.stream(prompt, confi):
        print(chunk)
        print("----")

    # print("Summary:", response)


if __name__ == "__main__":
    main()

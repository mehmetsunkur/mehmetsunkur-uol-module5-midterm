from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
import os

def extract_relevant_info(document_text, subject, api_key):
    try:
        # Set up OpenAI API key
        os.environ["OPENAI_API_KEY"] = api_key

        # Initialize the language model
        llm = OpenAI(temperature=0)

        # Create a Document object from the input text
        doc = Document(page_content=document_text)

        # Initialize text splitter
        text_splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separator="\n"
        )

        # Split the document into chunks
        texts = text_splitter.split_documents([doc])

        # Initialize the embedding model
        embeddings = OpenAIEmbeddings()

        # Create a vector store from the document chunks
        vectorstore = FAISS.from_documents(texts, embeddings)

        # Create a retrieval-based QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )

        # Format the query based on the subject
        query = f"What does the document say about {subject}? Please provide specific details and examples."

        # Get the response
        response = qa_chain({"query": query})

        return response["result"]

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Save the document text to a variable
    document_text = """[Your document text goes here]"""
    
    # Define the subject
    subject = "AI applications in medical diagnosis"
    
    # Replace with your actual OpenAI API key
    api_key = "your-api-key-here"
    
    # Extract relevant information
    result = extract_relevant_info(document_text, subject, api_key)
    print("\nExtracted relevant information:")
    print(result)
# Import necessary modules from LangChain
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
import os

# Set up OpenAI API key

def process_document(document_path, subject):
    # Initialize the LLM
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    
    # Load the markdown document
    loader = UnstructuredMarkdownLoader(document_path)
    documents = loader.load()
    
    # Split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200,
        separators=["\n\n", "\n", " ", ""]
    )
    splits = text_splitter.split_documents(documents)
    
    # Create map prompt template
    map_template = """Extract information related to {subject} from the following text:
    {text}
    
    Relevant information:"""
    map_prompt = PromptTemplate(template=map_template, input_variables=["subject", "text"])
    
    # Create reduce prompt template
    reduce_template = """Combine the following extracted information about {subject} into a coherent summary:
    {text}
    
    Combined summary:"""
    reduce_prompt = PromptTemplate(template=reduce_template, input_variables=["subject", "text"])
    
    # Create map chain
    map_chain = LLMChain(llm=llm, prompt=map_prompt)
    
    # Create reduce chain
    reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)
    
    # Create combine documents chain
    combine_documents_chain = StuffDocumentsChain(
        llm_chain=reduce_chain,
        document_variable_name="text"
    )
    
    # Create map reduce chain
    map_reduce_chain = MapReduceDocumentsChain(
        llm_chain=map_chain,
        combine_documents_chain=combine_documents_chain,
        document_variable_name="text",
        return_intermediate_steps=False
    )
    
    # Process the documents
    result = map_reduce_chain.run(
        input_documents=splits,
        subject=subject
    )
    
    return result

def main():
    # Example usage
    document_path = "/home/msunkur/dev/projects/uol/Module5/midterm/CM3020_Artificial_Intelligence/docs/OL-CM3020-Schaeffer-7038.md"
    subject = "Recent advancements in natural language processing"
    
    try:
        result = process_document(document_path, subject)
        print("\nFinal Summary:")
        print(result)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
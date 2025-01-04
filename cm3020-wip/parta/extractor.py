import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.document_loaders import TextLoader
from langchain_ollama import ChatOllama

import os
from pathlib import Path
import concurrent.futures

from langchain_openai import ChatOpenAI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MarkdownExtractorBruteForce:
    def __init__(self, markdown_file_path):
        """
        Initializes the MarkdownExtractorBruteForce class.

        :param markdown_file_path: Path to the Markdown document.
        :param openai_api_key: OpenAI API key for accessing GPT models.
        """
        self.file_path = markdown_file_path
        # Load the markdown document
        self.loader = UnstructuredMarkdownLoader(self.file_path)
        self.documents = self.loader.load()

        # self.documents = self._load_documents()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=4096*2, chunk_overlap=100)

        # self.llm = OpenAI(temperature=0)
        # base_url = 'https://5p4ls2pm92y2g0-11434.proxy.runpod.net'
        base_url = 'https://ntawj28avkaue3-11434.proxy.runpod.net'
        model = 'llama3.3'
        model = 'llama3.3:70b-instruct-q8_0'
        base_url = 'http://192.168.1.131:11434'
        model='gemma2:27b'
        self.llm = ChatOllama(
            model=model,
            temperature=0,
            max_tokens=500,
            num_ctx=4096*2,
            base_url=base_url,
        )

        self.qa_chain = load_qa_with_sources_chain(self.llm)

    def _load_documents(self):
        """
        Load the Markdown document.

        :return: List of documents.
        """
        loader = TextLoader(self.file_path)
        documents = loader.load()
        return documents

    def extract_section(self, query):
        """
        Extract relevant sections using a brute force approach.

        :param query: The subject or topic to search for.
        :return: Extracted sections with sources.
        """
        # Split the document into manageable chunks
        text_chunks = self.text_splitter.split_documents(self.documents)

        # Use QA chain to find relevant information in all chunks
        results = []
        logger.info("Number of chunks: %s", len(text_chunks))
        chunk_id = 0
        for chunk in text_chunks:

            # logger.info("Chunk: %s", chunk)
            response = self.qa_chain(
                {"input_documents": [chunk], "question": query})
            # logger.info("Response: %s", response)

            chunk_id += 1
            logger.info("Chunk %s:", chunk_id)
            response_text = response["output_text"]
            if (response_text == "not found"):
                logger.info("Response: %s", response_text)
                continue
            results.append(response["output_text"])

        # Combine and return all results
        combined_results = "\n\n".join(results)
        return combined_results


def process_file(markdown_file_path, query):
    extractor = MarkdownExtractorBruteForce(markdown_file_path)
    extracted_text = extractor.extract_section(query)
    logger.info("Extracted text from %s: %s", markdown_file_path, extracted_text)
    return extracted_text

# Usage example:
if __name__ == "__main__":
    # Replace with your markdown directory path and query
    markdown_dir_path = "./CM3020_Artificial_Intelligence/docs/"
    
    dir_path = Path(markdown_dir_path)
    markdown_files = [str(file) for file in dir_path.glob("*.md")]
    logger.info("Markdown files: %s", markdown_files)

    query = "1. Why do researchers create AI systems that play games? Respond as 'not found' if it does not have any information."

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        futures = {executor.submit(process_file, file, query): file for file in markdown_files}
        for future in concurrent.futures.as_completed(futures):
            file = futures[future]
            try:
                data = future.result()
            except Exception as exc:
                logger.error('%r generated an exception: %s' % (file, exc))

from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import Iterator
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document as LCDocument
from docling.document_converter import DocumentConverter

logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# class DoclingPDFLoader(BaseLoader):
#     def __init__(self, file_path: str | list[str]) -> None:
#         self._file_paths = file_path if isinstance(
#             file_path, list) else [file_path]
#         self._converter = DocumentConverter()

#     def lazy_load(self) -> Iterator[LCDocument]:
#         for source in self._file_paths:
#             dl_doc = self._converter.convert(source).document
#             text = dl_doc.export_to_markdown()
#             yield LCDocument(page_content=text)


# # FILE_PATH = "docs/OL-CM3020-Berliner.pdf"
# FILE_PATH = "CM3020_Artificial_Intelligence/docs/2412.11979v1.pdf"

# loader = DoclingPDFLoader(file_path=FILE_PATH)
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1000,
#     chunk_overlap=200,
# )
# # docs = loader.load()
# # splits = text_splitter.split_documents(docs)


# from docling.document_converter import DocumentConverter

# source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
# converter = DocumentConverter()
# result = converter.convert(FILE_PATH)
# print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"

import os
import multiprocessing as mp

def convert_pdf_to_md(pdf_path):
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    md_path = pdf_path.replace('.pdf', '.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(result.document.export_to_markdown())

def process_folder(folder_path):
    pdf_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    
    with mp.Pool(processes=5) as pool:
        pool.map(convert_pdf_to_md, pdf_files)

if __name__ == '__main__':
    folder_path = 'CM3005-Data-Science'  # Replace with your folder path
    process_folder(folder_path)

import logging
import os
import json
from venv import logger
from unstructured.staging.base import elements_to_json
from unstructured.partition.auto import partition
from io import StringIO
from lxml import etree
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    Iterator,
    List,
    Optional,
    Tuple,
    Type,
)

from unstructured import file_utils

from dotenv import load_dotenv, dotenv_values

from pathlib import Path
from unstructured_ingest.interfaces import (
    BaseDestinationConnector,
    BaseSourceConnector,
    ChunkingConfig,
    EmbeddingConfig,
    PartitionConfig,
    ProcessorConfig,
    ReadConfig,
    PermissionsConfig,
    ProcessorConfig,
    RetryStrategyConfig,
)

from unstructured_ingest.connector.local import LocalSourceConnector, SimpleLocalConfig
from unstructured_ingest.processor import process_documents


from unstructured.documents.elements import Element
from unstructured.staging.base import dict_to_elements


class ServiceUnstructured:
    logger = logging.getLogger(__name__)

    base_path = Path(__file__).parent / "docs" / "tmp"

    work_dir = base_path / "tmp_ingest"
    output_path = work_dir / "output"
    download_path = work_dir / "download"

    def setUp(self):
        self.output_path.mkdir(parents=True, exist_ok=True)
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self.download_path.mkdir(parents=True, exist_ok=True)

    def toJson(self, path: str, content_type: str) -> str:
        json_path = Path(path + ".json")
        if (json_path.exists()):
            return json_path.as_posix()

        doc_path: Path = Path(path)
        process_configs = ProcessorConfig(
            reprocess=False,          # Ignore cached content and reprocess if True
            verbose=True,             # Enable debug logging
            # Path for saving intermediate results

            work_dir=self.work_dir.resolve().as_posix(),
            output_dir=self.output_path.resolve().as_posix(),       # Path for final results
            num_processes=4,          # Number of workers to use in the pool
            raise_on_error=True      # Raise an error if any document fails

        )
        read_configs: ReadConfig = ReadConfig()

        local_connector = LocalSourceConnector(
            connector_config=SimpleLocalConfig(
                input_path=doc_path.as_posix()
                # recursive=True,
            ),
            read_config=read_configs,
            processor_config=process_configs,
        )
        additional_partition_args = {"extract_images_in_pdf": True, "extract_image_block_types": [
            "Image", "Table"], "extract_image_block_to_payload": False, "extract_image_block_output_dir": self.output_path.resolve().as_posix(), "metadata_page_number": True, "include_page_breaks": False}

        elements = partition(filename=path, content_type=content_type, strategy="hi_res", languages=["eng", "tur"], hi_res_model_name="yolox", skip_infer_table_types=[], **additional_partition_args)
        json_path: Path = Path(path + ".json")
        elements_to_json(elements=elements, filename=json_path)
        self.logger.info(json_path.as_posix)
        return json_path.as_posix()

    def iter_markdown_lines(self, elements: list[Element]) -> Iterator[str]:
        for e in elements:
            if e.category == "Title":
                yield f"# {e.text}\n"
            elif e.category == "ListItem":
                yield f"- {e.text}\n"
            else:
                yield f"{e.text}\n"

    def toMarkdown(self, path: str, content_type: str) -> str:
        markdown_path = Path(path + ".md")
        json_path = self.toJson(path, content_type)
        elements = self.get_elemnents_from_json(json_path)

        markdown_content = ''.join(self.iter_markdown_lines(elements))
        with open(markdown_path, 'w') as md_file:
            md_file.write(markdown_content)
        return markdown_path.as_posix()

    def get_elemnents_from_json(self, filepath: str) -> list[Element]:
        with open(filepath) as f:
            isd = json.load(f)
            elements:  list[Element] = dict_to_elements(isd)
            return elements


def worker(file_path):
    extractor = ServiceUnstructured()
    extractor.setUp()
    logger.info(f"Processing {file_path}")
    return extractor.toMarkdown(file_path, "pdf")


def process_files_parallel(folder_path: str, num_processes: int = 5):
    import multiprocessing as mp
    from pathlib import Path
    import glob

    pdf_files = glob.glob(f"{folder_path}/**/*.pdf", recursive=True)
    logger.info(f"Found {len(pdf_files)} files")
    with mp.Pool(processes=num_processes) as pool:
        results = pool.map(worker, pdf_files)
    return results


if __name__ == "__main__":
    folder_path = "./CM3005-Data-Science"
    results = process_files_parallel(folder_path, 5)
    print(f"Processed {len(results)} files")

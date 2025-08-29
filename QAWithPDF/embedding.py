from llama_index.core import VectorStoreIndex, Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import customexception
from logger import logging


def download_gemini_embedding(model, document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - query_engine: A query engine object to run semantic search on the index.
    """
    try:
        logging.info("Initializing Gemini embedding model...")

        # ✅ Use correct Gemini embedding model name
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")

        # ✅ Set global settings (new API)
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        logging.info("Creating VectorStoreIndex from documents...")
        index = VectorStoreIndex.from_documents(document)

        # ✅ Persist index to disk
        index.storage_context.persist()

        logging.info("Index creation successful. Returning query engine.")
        query_engine = index.as_query_engine()
        return query_engine

    except Exception as e:
        logging.error("Error occurred in download_gemini_embedding.")
        raise customexception(e, sys)

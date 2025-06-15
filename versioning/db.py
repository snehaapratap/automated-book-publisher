import chromadb
from chromadb.config import Settings

chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="chroma_data"))
collection = chroma_client.get_or_create_collection("chapter_versions")

def save_version(content, metadata):
    collection.add(documents=[content], metadatas=[metadata], ids=[metadata["version_id"]])

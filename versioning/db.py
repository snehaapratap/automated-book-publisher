import chromadb

# ✅ New Chroma Client (defaults to local and persistent)
client = chromadb.HttpClient(host="localhost", port=8000)  # if running ChromaDB as a server

# Or, for embedded mode:
# client = chromadb.PersistentClient(path="chroma_data")  # for local development

collection = client.get_or_create_collection(name="chapter_versions")

def save_version(content, metadata):
    collection.add(
        documents=[content],
        metadatas=[metadata],
        ids=[metadata["version_id"]]
    )

    
    
    
    
    
    
    
    
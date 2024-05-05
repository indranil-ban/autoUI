from enum import Enum
import chromadb # type: ignore

class CONSTANTS(str, Enum):
    COLLECTION_NAME = "component_embed"
    EMBED_MODEL = "all-mpnet-base-v2"
    CLIENT = chromadb.PersistentClient(path="/tmp/chromadb")
    NO_RESULTS=10
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

DATA_PATH = "./data"
CHROMA_PATH = "./chroma_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Split on all three header levels so each concept section becomes its own chunk
HEADERS_TO_SPLIT_ON = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

CHUNK_SIZE = 600    # wide enough for one full concept explanation
CHUNK_OVERLAP = 60  # 10% overlap so sentences at boundaries appear in both chunks


def load_documents():
    """Load every .md file under DATA_PATH as a LangChain Document."""
    loader = DirectoryLoader(
        DATA_PATH,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    return loader.load()


def split_documents(documents):
    """
    Two-pass split:
      1. MarkdownHeaderTextSplitter  — respects header boundaries, one chunk per section
      2. RecursiveCharacterTextSplitter — further splits any section still over CHUNK_SIZE
    Source file path is carried through to every chunk's metadata.
    """
    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=HEADERS_TO_SPLIT_ON,
        strip_headers=False,  # keep header text in the chunk so the LLM sees it
    )
    char_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    all_chunks = []
    for doc in documents:
        # Pass 1: split by Markdown headers
        header_chunks = header_splitter.split_text(doc.page_content)

        # Merge the original file's metadata (e.g. source path) into each header chunk
        for chunk in header_chunks:
            chunk.metadata.update(doc.metadata)

        # Pass 2: break oversized sections down further
        char_chunks = char_splitter.split_documents(header_chunks)
        all_chunks.extend(char_chunks)

    return all_chunks


def build_vectorstore(chunks):
    """Embed chunks and persist them to ChromaDB."""
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
        collection_metadata={"hnsw:space":"cosine"},
    )
    return vectorstore


def ingest():
    print(f"Loading documents from '{DATA_PATH}/' ...")
    documents = load_documents()
    print(f"  {len(documents)} file(s) loaded.")

    print("Splitting into chunks ...")
    chunks = split_documents(documents)
    print(f"  {len(chunks)} chunk(s) created.")

    print("Embedding and persisting to ChromaDB ...")
    build_vectorstore(chunks)
    print(f"  Done. Vector store saved to '{CHROMA_PATH}/'.")


if __name__ == "__main__":
    ingest()

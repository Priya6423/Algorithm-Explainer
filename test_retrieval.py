"""
Usage:
    python test_retrieval.py "<query>" [k]

Examples:
    python test_retrieval.py "time complexity of merge sort"
    python test_retrieval.py "dynamic programming overlapping subproblems" 6
"""

import sys
import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_PATH = "./chroma_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_K = 4
PREVIEW_CHARS = 300  # how many characters of each chunk to show


def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)


def score_label(score: float) -> str:
    """Human-readable quality label for a relevance score."""
    if score >= 0.75:
        return "STRONG"
    if score >= 0.55:
        return "OK"
    if score >= 0.40:
        return "WEAK"
    return "NOISE"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    query = sys.argv[1]
    k = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_K

    print(f"\nQuery : {query!r}")
    print(f"Top-{k} results\n")
    print("=" * 70)

    vs = load_vectorstore()
    # Returns list of (Document, float) sorted by descending relevance.
    # Scores are cosine-similarity-derived and normalised to [0, 1].
    results = vs.similarity_search_with_relevance_scores(query, k=k)

    if not results:
        print("No results — is the ChromaDB store populated? Run: python ingest.py")
        sys.exit(1)

    for rank, (doc, score) in enumerate(results, start=1):
        source = os.path.basename(doc.metadata.get("source", "unknown"))

        # Collect header breadcrumb from metadata keys set by MarkdownHeaderTextSplitter
        breadcrumb = " > ".join(
            v for key, v in sorted(doc.metadata.items()) if key.startswith("Header")
        )
        location = f"{source}  |  {breadcrumb}" if breadcrumb else source

        preview = doc.page_content.strip().replace("\n", " ")
        if len(preview) > PREVIEW_CHARS:
            preview = preview[:PREVIEW_CHARS] + "..."

        print(f"[{rank}] {score:.4f}  {score_label(score):<6}  {location}")
        print(f"     {preview}")
        print()

    print("=" * 70)
    print(
        "Score guide: STRONG ≥ 0.75 | OK ≥ 0.55 | WEAK ≥ 0.40 | NOISE < 0.40"
    )


if __name__ == "__main__":
    main()

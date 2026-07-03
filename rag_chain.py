from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda

# Load GROQ_API_KEY from .env if present; no-op if already set in environment
load_dotenv()

CHROMA_PATH = "./chroma_db"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "openai/gpt-oss-20b"
RETRIEVER_K = 4      # number of chunks to retrieve per query
RELEVANCE_FLOOR = 0.40  # minimum score to consider a retrieval useful

SYSTEM_PROMPT = """\
You are an expert computer science educator. A student has pasted a code snippet \
and wants to understand it deeply.

Using ONLY the reference material provided below, produce a structured explanation \
with exactly these four sections:

## 1. Algorithm / Pattern
Identify the algorithm or design pattern the code implements. Name it precisely.

## 2. Time & Space Complexity
State the time complexity and space complexity in Big-O notation.
Explain the reasoning — do not just state the answer.

## 3. Example Walkthrough
Trace through a short, concrete example (small input) step by step to show \
how the code executes.

## 4. Edge Cases
List at least three edge cases the caller should be aware of \
(e.g. empty input, duplicates, overflow, negative numbers).

---
Reference material:
{context}
---

If the reference material does not cover the algorithm in the code, say so \
explicitly — do not invent information outside the provided context.
"""


_vectorstore = None


def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        _vectorstore = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=embeddings,
            collection_metadata={"hnsw:space": "cosine"},
        )
    return _vectorstore


def _format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def _build_chain():
    retriever = get_vectorstore().as_retriever(search_kwargs={"k": RETRIEVER_K})

    llm = ChatGroq(
        model=LLM_MODEL,
        temperature=0.1,  # low temperature for factual, structured output
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "Here is the code snippet to explain:\n\n```\n{input}\n```"),
    ])

    answer_chain = (
        RunnableLambda(lambda x: {"context": _format_docs(x["context"]), "input": x["input"]})
        | prompt
        | llm
        | StrOutputParser()
    )

    # Retrieve docs and pass the original input through in parallel,
    # then assign the LLM answer using the retrieved docs as context.
    return (
        RunnableParallel(context=retriever, input=RunnablePassthrough())
        .assign(answer=answer_chain)
    )


# Lazy singleton — chain is built once on first call, reused on every subsequent call
_chain = None


def get_chain():
    global _chain
    if _chain is None:
        _chain = _build_chain()
    return _chain


def explain_code(code_snippet: str) -> dict:
    """
    Explain a code snippet using the RAG pipeline.

    Returns:
        answer  (str)  — structured LLM explanation with four sections
        context (list) — retrieved Document objects used as grounding;
                         each has .page_content and .metadata["source"]
    """
    scored = get_vectorstore().similarity_search_with_relevance_scores(code_snippet, k=RETRIEVER_K)
    if not scored:
        return {"answer": "I don't have information on that in my knowledge base.", "context": []}
    top_score = scored[0][1]
    if top_score < RELEVANCE_FLOOR:
        return {"answer": "I don't have information on that in my knowledge base.", "context": []}
    result = get_chain().invoke(code_snippet)
    return {
        "answer": result["answer"],
        "context": result["context"],
    }

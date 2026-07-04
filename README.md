---
title: Algorithm Explainer
emoji: 🧠
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# Algorithm Explainer

Paste a code snippet to identify the algorithm, get a complexity analysis, a step-by-step walkthrough, and edge cases — grounded in a curated CS knowledge base via RAG.

## Setup

**1. Clone and install dependencies**

```bash
git clone https://github.com/Priya6423/Algorithm-Explainer.git
cd Algorithm-Explainer
pip install -r requirements.txt
```

**2. Add your Groq API key**

Create a `.env` file in the project root (get a free key at [console.groq.com](https://console.groq.com/keys)):

```
GROQ_API_KEY=your_key_here
```

**3. Build the vector store**

The vector database (`chroma_db/`) is not committed to the repo — it's generated locally from the markdown files in `data/`:

```bash
python ingest.py
```

Re-run this any time you add or edit files under `data/`.

**4. Run the app**

```bash
streamlit run app.py
```

Open the local URL Streamlit prints (defaults to `http://localhost:8501`).

## Debugging retrieval

To inspect what chunks a query retrieves and their relevance scores, without spending an LLM call:

```bash
python test_retrieval.py "time complexity of merge sort"
```

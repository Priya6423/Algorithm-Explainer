import os
import streamlit as st
from rag_chain import explain_code

MIN_CHARS = 20   # fewer than this is not plausible code
MIN_LINES = 2    # single-word / one-liner inputs are rejected

st.set_page_config(
    page_title="Algorithm Explainer",
    page_icon="🧠",
    layout="centered",
)

st.title("🧠 Algorithm Explainer")
st.caption(
    "Paste a code snippet — the app identifies the algorithm, explains its "
    "complexity, walks through an example, and flags edge cases."
)

code_input = st.text_area(
    label="Code snippet",
    placeholder="def binary_search(arr, target):\n    ...",
    height=220,
    label_visibility="collapsed",
)

analyze_clicked = st.button("Analyze", type="primary", use_container_width=True)

if analyze_clicked:
    stripped = code_input.strip()

    if not stripped:
        st.warning("Paste a code snippet first.")
    elif len(stripped) < MIN_CHARS or len(stripped.splitlines()) < MIN_LINES:
        st.warning("That looks too short to be real code. Paste at least a full function.")
    else:
        with st.spinner("Retrieving concepts and generating explanation…"):
            result = explain_code(code_input)

        answer = result["answer"]
        context_docs = result["context"]

        st.divider()

        # ── Explanation ──────────────────────────────────────────────────────
        st.subheader("Explanation")
        st.markdown(answer)

        # ── Source chunks (collapsible) ──────────────────────────────────────
        st.divider()
        if context_docs:
            with st.expander(f"Sources retrieved ({len(context_docs)} chunks)"):
                for i, doc in enumerate(context_docs, start=1):
                    source = os.path.basename(doc.metadata.get("source", "unknown"))
                    breadcrumb = " › ".join(
                        v for k, v in sorted(doc.metadata.items()) if k.startswith("Header")
                    )
                    label = f"{source}  —  {breadcrumb}" if breadcrumb else source
                    st.caption(f"[{i}] {label}")
                    st.markdown(doc.page_content)
                    if i < len(context_docs):
                        st.divider()
        else:
            st.info(
                "No relevant chunks were retrieved — the knowledge base may not "
                "cover this algorithm."
            )

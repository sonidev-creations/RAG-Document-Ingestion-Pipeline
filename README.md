# Enterprise Fraud Analytics RAG Engine

A production-grade Retrieval-Augmented Generation (RAG) orchestration platform built to ingest multi-page compliance white papers dynamically, construct dense vector spatial indices, and provide an interactive terminal loop interface for real-time semantic discovery.

---

## 🏗️ Production Architecture vs. Baseline Implementations
Unlike baseline RAG assignments that rely on hardcoded static strings inside a single processing module, this platform implements a decoupled, event-driven infrastructure:

1. **Decoupled Processing Pipeline (`ingest.py`):** Opens physical data streams out of multi-page `.pdf` files from disk storage using programmatic abstraction layers, splits text systematically into context-insulated packets, and vectorizes structural fields into binary serialization indexes.
2. **Stateful Application Runtime (`search.py`):** An asynchronous interactive shell environment that hydrates local vector binaries into high-performance RAM instances instantly, supporting seamless, repetitive analytics probing without costly document reprocessing loops.

---

## 🛠️ Deep Technical Stack & Parameter Tuning
* **Core Framework:** LangChain Engine Abstractions (`langchain-huggingface`)
* **Vector Vector Store:** **FAISS (Facebook AI Similarity Search)** utilizing dense vector spatial clustering matrices.
* **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2` transforming text strings into robust 384-dimensional conceptual vectors.
* **Document Parsing Unit:** `pypdf` structural token extractor.
* **Matrix Segmentation Constants:**
  - `chunk_size`: 450 characters (Optimized mathematical window to map precise paragraphs cleanly).
  - `chunk_overlap`: 50 characters (Strategic sliding boundaries preventing informational loss across neighboring chunks).

---

## 📊 Evaluation Matrix & Operational Validation

### Test Case Execution
* **Target Analytical Query:** *"What civil penalty or fines were imposed on Wells Fargo for mortgage fraud?"*
* **Search Depth Factor ($k$):** Set to 2 ($k=2$) to ensure maximum structural context retrieval.

### Verified Live Output Metrics
```text
Analyzing semantic matches for: 'What civil penalty or fines were imposed on Wells Fargo for mortgage fraud?'...

  [MATCH #1] Verified Source: fighting-fraud-in-financial-services.pdf (Page 2)
  ----------------------------------------------------------------------
    The US Department of Justice has imposed a civil penalty of
    $2.09 billion on Wells Fargo under the Financial Institutions,
    Reform, Recovery, and Enforcement Act for originating and
    selling mortgage loans containing misstated income.
  ----------------------------------------------------------------------

  [MATCH #2] Verified Source: fighting-fraud-in-financial-services.pdf (Page 6)
  ----------------------------------------------------------------------
    3. US Department of Justice, Wells Fargo Agrees to Pay $2.09 Billion Penalty for
    Allegedly Misrepresenting Quality of Loans Used in Residential Mortgage-Backed...
  ----------------------------------------------------------------------
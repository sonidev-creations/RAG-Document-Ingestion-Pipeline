# Automated Fraud Analytics RAG Engine

A professional AI search engine that reads a physical financial fraud PDF report, converts it into searchable mathematical vectors, and lets you ask questions interactively through your terminal.

---

### Project Execution Interface
![Project Execution](Screenshot1.png)

---

## How It Works (The Pipeline Flow)

The project is split into two separate modules so you do not have to process the PDF every time you ask a question:

```text
[ 1. Ingestion Pipeline (ingest.py) ]
Physical PDF File -> Text Extraction -> Paragraph Chunks -> FAISS Database (Saved on disk)

[ 2. Interactive Application (search.py) ]
User Input Query -> FAISS Vector Search -> Terminal Prints Text + Page Citations
```

### Project Structure
- **`documents/`**: Folder containing your physical source document (`fighting-fraud-in-financial-services.pdf`).
- **`faiss_fraud_db/`**: The generated local vector database storage folder.
- **`ingest.py`**: Processes and indexes the text from the PDF file.
- **`search.py`**: Runs the interactive loop application in your terminal to search the database.

---

## Setup and Running Instructions

Follow these terminal steps to set up and run the engine:

### 1. Install Dependencies
```bash
pip install pypdf langchain-huggingface langchain-community faiss-cpu sentence-transformers
```

### 2. Build the Database
Run the ingestion script to parse your PDF file and compile the local FAISS index:
```bash
python ingest.py
```

### 3. Run the Search App
Launch the interactive terminal search prompt:
```bash
python search.py
```

---

## Sample Queries to Try

Once the app is running, paste these queries into the terminal to test the system:
- *"What civil penalty or fines were imposed on Wells Fargo for mortgage fraud?"*
- *"What are the key trends driving next-gen approaches in fraud detection?"*

*(Type `exit` to quit the interactive search application).*

---

### Push the update to GitHub
Once you save the code above into your local `README.md` file, run these commands in your terminal to update your repository online:

```bash
git add README.md
git commit -m "docs: simplify readme content and layout"
git push origin main
```

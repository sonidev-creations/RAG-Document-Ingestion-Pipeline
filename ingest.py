import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_TOKEN"] = ""

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def main():
    print("=== STARTING VECTOR DATABASE INGESTION PIPELINE ===")

    pdf_path = os.path.join("documents", "fighting-fraud-in-financial-services.pdf")
    db_folder = "faiss_fraud_db"
    
    if not os.path.exists(pdf_path):
        print(f"[ERROR] Could not find the PDF file at: {pdf_path}")
        print("Please create a 'documents/' folder and place your PDF file inside it.")
        return
    print(f"\n[Step 1/4] Extracting text directly from physical file: {pdf_path}...")
    loader = PyPDFLoader(pdf_path)
    raw_documents = loader.load()
    print(f" -> Successfully loaded {len(raw_documents)} raw document pages.")
    print("\n[Step 2/4] Splitting extracted text into paragraph-sized chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=450,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )
    semantic_chunks = text_splitter.split_documents(raw_documents)
    print(f" -> Generated {len(semantic_chunks)} clean semantic text segments.")

    print("\n[Step 3/4] Initializing semantic embedding model (all-MiniLM-L6-v2)...")
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("\n[Step 4/4] Generating vector math matrices and building local FAISS index...")
    vector_db = FAISS.from_documents(semantic_chunks, embedding_model)
    
    vector_db.save_local(db_folder)
    print(f"\n=== SUCCESS! Local Vector Store compiled securely at: '{db_folder}/' ===")

if __name__ == "__main__":
    main()
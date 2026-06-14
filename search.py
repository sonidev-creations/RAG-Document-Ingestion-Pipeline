import os
import sys

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_TOKEN"] = ""

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def main():
    db_folder = "faiss_fraud_db"
    
    if not os.path.exists(db_folder):
        print(f"[ERROR] Local vector database '{db_folder}' does not exist.")
        print("Please execute 'python ingest.py' first to build and store the index.")
        sys.exit(1)
    
    print("Connecting to local FAISS vector directory...")
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.load_local(db_folder, embedding_model, allow_dangerous_deserialization=True)
    print("Database connected. Semantic search context engine online.")
    print("==========================================================================")
    print("       Welcome to the Enterprise Fraud Analytics RAG Search Engine        ")
    print("      Type your research questions below. Enter 'exit' to terminate.      ")
    print("==========================================================================")

    while True:
        try:
            print("\n" + "_" * 80)
            user_query = input("\nEnter Search Query: ").strip()
            
            if user_query.lower() == 'exit':
                print("\nShutting down engine connection. Goodbye!")
                break
                
            if not user_query:
                print("[Warning] Query input string cannot be blank.")
                continue

            print(f"Analyzing semantic matches for: '{user_query}'...")
            
            
            search_results = vector_db.similarity_search(user_query, k=2)
            
            if not search_results:
                print("\n[No Matches] The data repository returned zero semantic overlapping items.")
                continue
        
            for idx, match in enumerate(search_results):
                page_num = match.metadata.get('page', 0) + 1  
                source_doc = os.path.basename(match.metadata.get('source', 'Unknown Document'))
                
                print(f"\n  [MATCH #{idx + 1}] Verified Source: {source_doc} (Page {page_num})")
                print(f"  " + "-" * 70)
                clean_lines = match.page_content.strip().split('\n')
                for line in clean_lines:
                    if line.strip():
                        print(f"    {line.strip()}")
                print(f"  " + "-" * 70)

        except KeyboardInterrupt:
            print("\n\nSession interrupted safely. Exiting application engine.")
            break

if __name__ == "__main__":
    main()
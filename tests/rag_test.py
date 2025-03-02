import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.rag_client import run_rag, RAG_Client

# result = run_rag('李白的出生地点', knowledge_base_path='src/rag/kdb')

# print(result)

if __name__ == "__main__":
    rag_client = RAG_Client()
    result = rag_client.query("李白的出生地点")
    print(result)

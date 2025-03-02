import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.rag_client import run_rag, RAG_Client

# result = run_rag('李白的出生地点', knowledge_base_path='src/rag/kdb')

# print(result)

if __name__ == "__main__":
    rag_client = RAG_Client()
    keyword = rag_client.get_query_key("李白是哪里人？有哪些作品？")
    print(keyword)
    result = rag_client.query(keyword)
    # result = rag_client.query("李白是哪里人？有哪些作品？")
    print(result)

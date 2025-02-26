import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.rag_client import run_rag

result = run_rag('AgentChatBot是一个什么类型的项目', knowledge_base_path='src/rag/kdb')

print(result)

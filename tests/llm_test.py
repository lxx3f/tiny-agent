import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm.base import DouBaoService


def test_doubao_call():
    llm_service = DouBaoService()
    prompt = "一句话回答：故障机器人是不是尖塔最强角色？"
    response = llm_service.call(prompt)
    assert response
    print(response)


def test_a_call():
    llm_service = DouBaoService()
    prompt = input()
    response = llm_service.call(prompt)
    assert response
    print(response)


import os
from openai import OpenAI
from src.config.settings import DOUBAO_EMBEDDING_DATA

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(api_key=DOUBAO_EMBEDDING_DATA["api_key"],
                base_url=DOUBAO_EMBEDDING_DATA["base_url"])

print("----- embeddings request -----")
resp = client.embeddings.create(model="doubao-embedding-text-240715",
                                input=["花椰菜又称菜花、花菜，是一种常见的蔬菜。"],
                                encoding_format="float")
print(resp)

if __name__ == "__main__":
    test_doubao_call()
    # test_a_call()

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


if __name__ == "__main__":
    test_doubao_call()
    # test_a_call()

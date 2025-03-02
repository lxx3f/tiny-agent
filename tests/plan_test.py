import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.agent.plan import Planner
from src.agent.memory import MemoryItem


def test_create_plan():
    planner = Planner()
    history = []

    user_message = "今天天气真好"
    plan = planner.create_plan(user_message, history)
    assert plan
    print(plan)


if __name__ == '__main__':
    test_create_plan()

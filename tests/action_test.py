import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent.action import ActionExecutor


def test_action():
    executor = ActionExecutor()
    executor.execute("chat", response="你好呀~")


if __name__ == "__main__":
    test_action()

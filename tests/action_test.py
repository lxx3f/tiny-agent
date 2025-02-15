import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent.action import ActionExecutor


def test_action():
    executor = ActionExecutor()
    executor.execute("chat", response="你好呀~")
    executor.execute("ask_gift", response="111", gift_name="布偶")
    executor.execute("give_gift", response="zzz", gift_name="巧克力")
    executor.execute("intimate_action", response="bb", action="拥抱")


if __name__ == "__main__":
    test_action()

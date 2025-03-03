from typing import Any
from src.tools.base import Tool


class ChatTool(Tool):

    def name(self) -> str:
        return "chat"

    def description(self) -> str:
        return """
向用户发送消息
输入:
- response: str, 你的回复内容
输出:
- None
"""

    def run(self, response: str, **kwargs) -> Any:
        # TODO
        print(f"\n{response}")
        return None

    def format_result(self, result: Any, params: dict):
        response = params.get("response", "")
        return f"回复: {response}"


class NullTool(Tool):

    def name(self):
        return "null"

    def description(self):
        return """
空动作，什么也不做
输入:
- None
输出：
- None
"""

    def run(self) -> Any:
        return None

    def format_result(self, result, params):
        return ""

from typing import Any
from src.tools.base import Tool


class Send_Email_Tool(Tool):

    def name(self) -> str:
        return "send_email"

    def description(self) -> str:
        return """
发送邮件
输入:
- receiver: str, 目的邮箱地址
- response: str, 邮件正文内容
输出:
- None
"""

    def run(self, receiver: str, response: str, **kwargs) -> Any:
        # TODO
        print(f"正在发送邮件:\n")
        print(f"收件地址:{receiver}\n")
        print(f"正文内容:\n{response}")
        return None

    def format_result(self, result: Any, params: dict):
        response = params.get("response", "")
        receiver = params.get("receiver", "")
        return f"向{receiver}发送邮件成功\n"

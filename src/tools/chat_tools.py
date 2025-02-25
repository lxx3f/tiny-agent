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


# class GiveGiftTool(Tool):

#     def name(self) -> str:
#         return "give_gift"

#     def description(self) -> str:
#         return """
# 送给用户礼物
# 输入:
# - response: str, 你的送礼物的话语
# - gift_name: str, 要送的礼物名称
# 输出:
# - None
# """

#     def run(self, response: str, **kwargs) -> Any:
#         print(f"\n{response}")
#         return None

#     def format_result(self, result: Any, params: dict):
#         return ""

# class AskGiftTool(Tool):

#     def name(self) -> str:
#         return "ask_gift"

#     def description(self) -> str:
#         return """
# 向用户索要礼物
# 输入:
# - response: str, 你的请求礼物的话语
# - gift_name: str, 想要的礼物名称
# 输出:
# - gift_given: bool, 用户是否同意送礼物
# """

#     def run(self, response: str, gift_name: str, **kwargs) -> Any:
#         print(f"\n{response}")
#         print(f"\n想要的礼物是: {gift_name}")
#         user_input = input("\n是否愿意送出这个礼物？(y/n):").lower()
#         return user_input.startswith('y')

#     def format_result(self, result: Any, params: dict) -> str:
#         if result:
#             return f"用户同意了送给你{params['gift_name']}"
#         else:
#             return "用户拒绝了送礼物的请求"

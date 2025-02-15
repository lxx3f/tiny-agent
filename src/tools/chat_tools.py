from typing import Any
from src.tools.base import Tool


class ChatTool(Tool):

    def name(self) -> str:
        return "chat"

    def description(self) -> str:
        return """
继续和用户聊天
输入:
- response: str, 你的回复内容
输出:
- None
"""

    def run(self, response: str, **kwargs) -> Any:
        print(f"\n{response}")
        return None


class GiveGiftTool(Tool):

    def name(self) -> str:
        return "give_gift"

    def description(self) -> str:
        return """
送给用户礼物
输入:
- response: str, 你的送礼物的话语
- gift_name: str, 要送的礼物名称
输出:
- None
"""

    def run(self, response: str, **kwargs) -> Any:
        print(f"\n{response}")
        return None


class AskGiftTool(Tool):

    def name(self) -> str:
        return "ask_gift"

    def description(self) -> str:
        return """
向用户索要礼物
输入:
- response: str, 你的请求礼物的话语
- gift_name: str, 想要的礼物名称
输出:
- gift_given: bool, 用户是否同意送礼物
"""

    def run(self, response: str, gift_name: str, **kwargs) -> Any:
        print(f"\n{response}")
        print(f"\n想要的礼物是: {gift_name}")
        user_input = input("\n是否愿意送出这个礼物？(y/n):").lower()
        return user_input.startswith('y')


class IntimateActionTool(Tool):

    def name(self) -> str:
        return "intimate_action"

    def description(self) -> str:
        return """
对用户执行亲昵动作
输入:
- response: str, 你的话语
- action: str, 要执行的亲昵动作
输出:
- None
"""

    def run(self, response: str, action: str, **kwargs) -> Any:
        print(f"\n{response}")
        print(f"\n[执行动作]: {action}")
        return None

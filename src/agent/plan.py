from typing import List
from src.agent.memory import MemoryItem
from src.llm.base import DouBaoService
from src.prompts.builder import build_plan_prompt


class Planner:
    """
    planner module
    """

    def __init__(self):
        self.llm = DouBaoService()

    def create_plan(self, user_message: str, history: List[MemoryItem]) -> str:
        """
        根据历史记忆生成plan prompt,并调用llm生成response prompt
        
        user_message: 用户输入的消息
        history: 历史对话记录
        """
        prompt = build_plan_prompt(user_message, history)
        # print(f"plan prompt: \n{prompt}")
        return self.llm.call(prompt)

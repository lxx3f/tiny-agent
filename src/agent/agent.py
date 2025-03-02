from typing import Any, Dict, List, Tuple
import json
from src.agent.plan import Planner
from src.agent.memory import Memory
from src.agent.action import Action, ActionExecutor
from src.llm.base import DouBaoService
from src.prompts.builder import build_response_prompt
from src.rag.rag_client import RAG_Client


class Agent:
    """
    agent class
    """

    def __init__(self):
        self.memory = Memory()
        self.planner = Planner()
        self.llm = DouBaoService()
        self.executor = ActionExecutor()
        self.rag_client = RAG_Client()

    async def process_input(self, user_message: str) -> str:
        """
        处理用户输入,生成回复
        """
        # 存入记忆
        await self.memory.add_memory(user_message, memory_type="user")
        # 生成规划prompt
        plan: str = self.planner.create_plan(user_message, self.memory.memory)
        # 查询RAG知识库
        keyword = self.rag_client.get_query_key(user_message)
        rag_reslut = self.rag_client.query(keyword)
        # 调用llm获取回复
        response: str = self._gen_response(user_message, plan, rag_reslut)
        action_list: List = self._parse_response(response)

        for action in action_list:
            action_name = action.get("name", "")
            params = action.get("params", {})

            action = self.executor.execute(action_name, **params)
            if action_name == "null":
                break
            await self.memory.add_memory(action.result, memory_type="action")

        return action.result

    def _gen_response(self,
                      user_message: str,
                      plan: str,
                      rag_result: List[str] = []) -> str:
        """
        调用llm获取response
        """
        prompt = build_response_prompt(user_message=user_message,
                                       plan=plan,
                                       history=self.memory.memory,
                                       rag_result=rag_result)
        # print(prompt)
        # print()
        return self.llm.call(prompt)

    def _parse_response(self, response: str) -> Tuple[str, Dict[str, Any]]:
        """
        解析response
        """
        try:
            action_data = json.loads(response)
            return action_data
        except json.JSONDecodeError:
            print(f"解析响应失败: {response}")
            return []

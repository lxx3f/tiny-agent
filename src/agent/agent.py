from typing import Any, Dict, List, Tuple
import json
from src.agent.plan import Planner
from src.agent.memory import Memory
from src.agent.action import Action, ActionExecutor
from src.llm.base import LLMService, DouBaoService
from src.prompts.builder import build_response_prompt


class Agent:
    """
    agent class
    """

    def __init__(self):
        self.memory = Memory()
        self.planner = Planner()
        self.llm = DouBaoService()
        self.executor = ActionExecutor()

    async def process_input(self, user_message: str) -> str:
        """
        处理用户输入,生成回复
        """
        # 存入记忆
        await self.memory.add_memory(user_message, memory_type="user")
        # 生成规划prompt
        plan: str = self.planner.create_plan(user_message, self.memory.memory)
        # 调用llm获取回复
        response: str = self._gen_response(user_message, plan)
        thought, data = self._parse_response(response)
        cur_actions: List[Action] = []

        while data != {}:
            action_name = data.get("name", "")
            params = data.get("params", {})

            action = self.executor.execute(action_name, **params)
            cur_actions.append(action)

            tool = self.executor.tool_registry.get_tool(action_name)
            if action_name in ["end", "chat"]:
                await self.memory.add_memory(thought, memory_type="ai")
                break

            await self.memory.add_memory(thought, memory_type="ai")
            result_text = tool.format_result(action.result, action.params)
            await self.memory.add_memory(result_text,
                                         memory_type="action_result")

            response = self._gen_response(user_message, plan, cur_actions)
            thought, data = self._parse_response(response)

        return thought

    # 调用llm获取response
    def _gen_response(self,
                      user_message: str,
                      plan: str,
                      actions: List[Action] = []) -> str:
        prompt = build_response_prompt(user_message=user_message,
                                       plan=plan,
                                       actions=actions,
                                       history=self.memory.memory)
        print(prompt)
        print()
        return self.llm.call(prompt)

    def _parse_response(self, response: str) -> Tuple[str, Dict[str, Any]]:
        try:
            data = json.loads(response)
            thought = data.get("response", "")
            action_data = data.get("action", {})
            return thought, action_data
        except json.JSONDecodeError:
            print(f"解析响应失败: {response}")
            return "", {}

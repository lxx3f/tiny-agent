from typing import Any, Dict, List, Tuple
from agent.plan import Planner
from agent.memory import Memory
from agent.action import Action, ActionExecutor


class Agent:

    def __init__(self):
        self.memory = Memory()
        self.planner = Planner()
        self.executor = ActionExecutor()

    def process_input(self, user_message: str) -> str:
        plan: str = self.planner.create_plan(user_message)
        response: str = self._gen_response(user_message, plan)
        thought, data = self._parse_response(response)
        actions: List[Action] = []
        while data != {} and data.get("action_name", "end") != "end":
            action_name = data.get("action_name", "")
            params = data.get("params", {})
            action = self.executor.execute(action_name, **params)
            actions.append(action)
            response = self._gen_response(user_message, plan, actions)
            thought, data = self._parse_response(response)
        self.memory.add_memory(user_message, thought, actions)
        return thought

    def _gen_response(self,
                      user_message: str,
                      plan: str,
                      actions: List[Action] = []) -> str:
        pass

    def _parse_response(self, response: str) -> Tuple[str, Dict[str, Any]]:
        pass

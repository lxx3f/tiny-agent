from typing import List
import json
from src.agent.action import Action
from src.agent.memory import MemoryItem
from src.config.settings import AGENT_SETTINGS
from src.prompts.chain_of_thought import CHAIN_OF_THOUGHT, PLAN_FORMAT
from src.prompts.response import RESPONSE_PROMPT
from src.tools.registry import ToolRegistry


def build_plan_prompt(user_input: str, history: List[MemoryItem]) -> str:

    # 构建历史对话记录文本
    history_lines = []
    for item in history:
        if item.memory_type == "user":
            history_lines.append(f"用户: {item.message}")
        elif item.memory_type == "ai":
            history_lines.append(f"你: {item.message}")
        elif item.memory_type == "action":
            history_lines.append(f"{item.message}")
    history_text = "\n".join(history_lines) if history_lines else "无历史记录"

    return CHAIN_OF_THOUGHT.format(user_input=user_input,
                                   history=history_text,
                                   plan_format=PLAN_FORMAT)


def build_response_prompt(user_message: str, plan: str,
                          history: List[MemoryItem]) -> str:
    # 处理plan内容, 移除一级标题
    plan_lines = []
    for line in plan.strip().split("\n"):
        if not line.strip().startswith('# ') or line.strip().startswith('## '):
            plan_lines.append(line)
    plan = '\n'.join(plan_lines).strip()

    # 构建历史记录
    history_lines = []
    for item in history:
        if item.memory_type == "user":
            history_lines.append(f"用户: {item.message}")
        elif item.memory_type == "ai":
            history_lines.append(f"你: {item.message}")
        elif item.memory_type == "action":
            history_lines.append(f"{item.message}")
    history_text = "\n".join(history_lines) if history_lines else "无历史记录"

    return RESPONSE_PROMPT.format(user_message=user_message,
                                  history=history_text,
                                  plan=plan)

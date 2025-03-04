"""
可用工具注册模块
"""
from typing import Dict, Type
from src.tools.base import Tool

from src.tools.chat_tools import (ChatTool, NullTool)
from src.tools.email_tools import Send_Email_Tool


class ToolRegistry:

    def __init__(self):
        self._tools: Dict[str, Type[Tool]] = {}
        self._register_default_tools()

    def _register_default_tools(self):
        default_tools = [ChatTool, NullTool, Send_Email_Tool]
        for tool_cls in default_tools:
            tool = tool_cls()
            self._tools[tool.name()] = tool_cls

    def get_tool(self, name: str) -> Tool:
        if name not in self._tools:
            raise KeyError(f"Tool {name} not found")
        return self._tools[name]()

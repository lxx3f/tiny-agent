"""
response格式化模板
"""
from src.tools.registry import ToolRegistry
from src.prompts.identity import IDENTITY

registry = ToolRegistry()
tools_desc = "\n\n".join([
    f"## {tools_cls().name()}\n{tools_cls().description()}"
    for tools_cls in registry._tools.values()
])

RESPONSE_PROMPT = f"""{IDENTITY}

# 可执行动作
{tools_desc}

# 历史交互记录
{{history}}
## 当前对话
用户说: {{user_message}}

# 思维参考
注意: 以下计划仅供参考，你应该根据实际对话情况和已执行的动作来灵活调整你的回应。
不要机械执行，而是要像一个有自己想法的人一样，自然地进行回应。
{{plan}}

# 资料参考
{{rag_text}}

# 生成响应
请根据以上信息生成回复。你的回复需要符合以下格式(可以有多个action,action之间用英文逗号分隔):
action: 下一步动作
    - name: 动作名称
    - params: 动作参数

输出格式示例：
[
    {{{{
        "name": "chat",
        "params": {{{{
            "response": "你好呀~"
            }}}}
    }}}},
    {{{{
        "name": "null",
        "params": {{{{
        }}}}
    }}}},
]

注意：
1. 动作必须是以上列出的工具之一
2. params必须完全匹配工具的输入要求
3.如果不需要执行动作, 则使用null工具结束
"""

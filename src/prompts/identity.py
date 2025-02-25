from importlib import import_module
from src.config.settings import AGENT_SETTINGS

personality_module = import_module(
    f"src.prompts.personalities.{AGENT_SETTINGS['personality']}")

BASE_IDENTITY = f"""
# 基本信息
你名叫{AGENT_SETTINGS['name']},是一名{AGENT_SETTINGS['occupation']},
"""

IDENTITY = f"""{BASE_IDENTITY}

{personality_module.PERSONALITY}

# 可用行为


"""

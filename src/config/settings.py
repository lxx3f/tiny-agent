# memory
MEMORY_SIZE = 20

# llm
DOUBAO_SETTINGS = {
    "api_key": "a07bb9a3-5413-43f6-9a62-9de197fd0152",
    "base_url": "https://ark.cn-beijing.volces.com/api/v3",
    "model": "ep-20250213235435-rpbp7"
}

# agent personality
_AGENT_SETTING_ASSISTANT = {"personality": "assistant", "name": "鸡煲"}

AGENT_SETTINGS = _AGENT_SETTING_ASSISTANT

# logging
log_filename_agent = "logs/app.log"
# log_filename_llm = "logs/llm.log"
import logging


def setup_logging():
    logging.basicConfig(filename=log_filename_agent,
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

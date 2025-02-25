from openai import OpenAI
from abc import ABC, abstractmethod
from src.config.settings import DOUBAO_SETTINGS
import logging


class LLMService(ABC):

    @abstractmethod
    def call(self, prompt: str) -> str:
        pass


class DouBaoService(LLMService):

    def __init__(self):
        super().__init__()
        self._llm_client = OpenAI(
            api_key=DOUBAO_SETTINGS["api_key"],
            base_url=DOUBAO_SETTINGS['base_url'],
        )

    def call(self, prompt: str) -> str:
        logging.info("call doubao:" + prompt)
        response = self._llm_client.chat.completions.create(
            model=DOUBAO_SETTINGS["model"],
            messages=[{
                "role": "system",
                "content": "你是豆包，是由字节跳动开发的 AI 人工智能助手"
            }, {
                "role": "user",
                "content": prompt
            }])
        return response.choices[0].message.content.strip()

from typing import List
from openai import OpenAI

from src.config.settings import DOUBAO_EMBEDDING_DATA


class EmbeddingModel:
    """
    向量模型客户端
    """

    def __init__(self) -> None:
        """
        初始化
        """
        self.client = OpenAI(api_key=DOUBAO_EMBEDDING_DATA["api_key"],
                             base_url=DOUBAO_EMBEDDING_DATA["base_url"])

    def get_embedding(self, text: str) -> List[float]:
        """
        text (str) - 需要转化为向量的文本
        
        return：list[float] - 文本的向量表示
        """
        # 去掉文本中的换行符，保证输入格式规范
        text = text.replace("\n", " ")
        return self.client.embeddings.create(
            model=DOUBAO_EMBEDDING_DATA["model"],
            input=[text],
            encoding_format="float",
        ).data[0].embedding

from typing import List, Dict
from src.rag.vectorstore import VectorStore
from src.rag.embedding import EmbeddingModel
from src.utils.load_file import ReadFiles
from src.config.settings import (RAG_DEFAULT_SAVE_PATH,
                                 RAG_DEFAULT_KNOWLEDGE_BASE_PATH,
                                 RAG_MAX_TOKEN_LEN, RAG_COVER_LEN,
                                 RAG_TEXT_NUMS)


def run_rag(question: str,
            knowledge_base_path: str = RAG_DEFAULT_KNOWLEDGE_BASE_PATH,
            k: int = 1) -> str:
    """
    :param question: 用户提出的问题
    :param knowledge_base_path: 知识库的路径，包含文档的文件夹路径
    :param k: 返回与问题最相关的k个文档片段，默认为1
    :return: 返回从知识库查询到的相关内容
    """
    # 加载并切分文档
    docs = ReadFiles(knowledge_base_path).get_content(
        max_token_len=RAG_MAX_TOKEN_LEN, cover_content=RAG_COVER_LEN)
    vector = VectorStore(docs)

    # 创建向量模型客户端
    embedding = EmbeddingModel()
    vector.get_vector(EmbeddingModel=embedding)

    # 将向量和文档保存到本地
    vector.persist(path=RAG_DEFAULT_SAVE_PATH)

    # 打印数据信息
    vector.print_info()

    # 在数据库中检索最相关的文档片段
    content = vector.query(question, EmbeddingModel=embedding, k=k)[0]

    return content


class RAG_Client():
    """
    RAG代理类
    """

    def __init__(self, knowledge_base_path: str = RAG_DEFAULT_SAVE_PATH):
        # 加载并切分文档
        docs = ReadFiles(knowledge_base_path).get_content(
            max_token_len=RAG_MAX_TOKEN_LEN, cover_content=RAG_COVER_LEN)

        self.vector = VectorStore(docs)

        # 创建向量模型客户端
        self.embedding = EmbeddingModel()
        self.vector.get_vector(EmbeddingModel=self.embedding)

        # 将向量和文档保存到本地
        self.vector.persist(path=RAG_DEFAULT_SAVE_PATH)

    def query(self, query: str, k: int = RAG_TEXT_NUMS) -> List[str]:
        """
        根据用户的查询文本，检索最相关的文档片段。
        :param query: 用户的查询文本。
        :param k: 返回最相似的文档数量，默认为1
        :return: 返回最相似文档内容列表。
        """
        result: List[Dict[str,
                          str]] = self.vector.query(query, self.embedding, k)
        contents = [x["document"] for x in result]
        return contents

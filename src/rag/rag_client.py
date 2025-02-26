from src.rag.vectorstore import VectorStore
from src.rag.embedding import EmbeddingModel
from src.utils.load_file import ReadFiles
from src.config.settings import RAG_DEFAULT_SAVE_PATH


def run_rag(question: str, knowledge_base_path: str, k: int = 1) -> str:
    """
    :param question: 用户提出的问题
    :param knowledge_base_path: 知识库的路径，包含文档的文件夹路径
    :param k: 返回与问题最相关的k个文档片段，默认为1
    :return: 返回从知识库查询到的相关内容
    """
    # 加载并切分文档
    docs = ReadFiles(knowledge_base_path).get_content(max_token_len=600,
                                                      cover_content=150)
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

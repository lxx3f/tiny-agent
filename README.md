# 简介
用python编写的简单agent框架。
基于大语言模型的智能助理。

# 功能
- 基于本地知识库的信息查询和整理(联网查询功能待完成)
- 智能对话
- 自定义工具扩展

# 项目结构
```
agent
├─ main.py # 程序入口
├─ README.md
├─ requirements.txt 
├─ src
│  ├─ agent # agent基类和核心模块
│  │  ├─ action.py # 行为执行模块
│  │  ├─ agent.py # agent基类
│  │  ├─ memory.py # 记忆模块，保存短期记忆
│  │  ├─ plan.py # 规划模块，划分子任务
│  │  └─ __init__.py
│  ├─ config
│  │  ├─ settings.py # 参数设置
│  │  └─ __init__.py
│  ├─ llm # 提供大模型调用服务
│  │  ├─ base.py 
│  │  └─ __init__.py
│  ├─ prompts 
│  │  ├─ builder.py # 构造prompts
│  │  ├─ chain_of_thought.py # 思维链模板
│  │  ├─ identity.py # agent身份描述
│  │  ├─ personalities # agent人设
│  │  │  ├─ assistant.py
│  │  │  └─ __init__.py
│  │  ├─ rag.py # RAG相关prompts
│  │  ├─ response.py
│  │  └─ __init__.py
│  ├─ rag # RAG模块
│  │  ├─ documents.py # 文件基类
│  │  ├─ embedding.py # 文本嵌入(文本转向量)
│  │  ├─ kdb # 知识库
│  │  │  ├─ 刘过.md
│  │  │  ├─ 李白.md
│  │  │  └─ 柳永.md
│  │  ├─ rag_client.py # 提供RAG服务
│  │  ├─ storage # 本地知识库
│  │  │  ├─ documents.txt 
│  │  │  ├─ vectors.npy # 知识库的向量存储
│  │  │  └─ vector_ids.txt
│  │  ├─ vectorstore.py # 向量知识库的保存和读取
│  │  └─ __init__.py
│  ├─ tools # 提供agent对外部操作的工具
│  │  ├─ base.py
│  │  ├─ chat_tools.py
│  │  ├─ registry.py
│  │  └─ __init__.py
│  ├─ ui 
│  │  └─ __init__.py
│  └─ utils # 基础工具集
│     ├─ load_file.py
│     └─ __init__.py
├─ tests # 功能测试
│  ├─ action_test.py
│  ├─ llm_test.py
│  ├─ plan_test.py
│  └─ rag_test.py
└─ __init__.py

```

# 相关项目
[agent_chat_wechat](https://github.com/panxingfeng/agent_chat_wechat): RAG部分的实现参考了该项目
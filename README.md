
# project structure

```
agent
├─ README.md
├─ requirements.txt
├─ src
│  ├─ agent
│  │  ├─ action.py
│  │  ├─ base.py
│  │  ├─ memory.py
│  │  ├─ plan.py
│  │  └─ __init__.py
│  ├─ config
│  │  ├─ settings.py
│  │  └─ __init__.py
│  ├─ llm
│  │  ├─ base.py
│  │  └─ __init__.py
│  ├─ prompts
│  │  ├─ builder.py
│  │  ├─ chain_of_thought.py
│  │  ├─ identity.py
│  │  ├─ personalities
│  │  │  ├─ cute.py
│  │  │  └─ __init__.py
│  │  ├─ response.py
│  │  └─ __init__.py
│  ├─ rag
│  │  └─ __init__.py
│  ├─ tools
│  │  ├─ base.py
│  │  ├─ chat_tools.py
│  │  ├─ registry.py
│  │  └─ __init__.py
│  ├─ ui
│  │  └─ __init__.py
│  └─ utils
│     └─ __init__.py
├─ tests
│  ├─ action_test.py
│  ├─ llm_test.py
│  └─ plan_test.py
└─ __init__.py

```
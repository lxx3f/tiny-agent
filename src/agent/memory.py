import asyncio
from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Literal

from src.config.settings import MEMORY_SIZE
from src.agent.action import Action


@dataclass
class MemoryItem:
    message: str
    memory_type: Literal["user", "ai", "action_result"]
    timestamp: datetime


class Memory:

    def __init__(self):
        self._memories: List[MemoryItem] = []

    async def add_memory(
        self,
        message: str,
        memory_type: Literal["user", "ai", "action_result"],
    ) -> None:
        memory_item = MemoryItem(message=message,
                                 memory_type=memory_type,
                                 timestamp=datetime.now())
        self._memories.append(memory_item)
        # 超出短期记忆大小则将旧的记忆存入RAG
        if len(self._memories) > MEMORY_SIZE:
            long_term_mem = self._memories[0]
            self._memories.pop(0)
            asyncio.create_task(self._save_to_rag(long_term_mem))

    async def _save_to_rag(self, memory_item: MemoryItem) -> None:
        # TODO: 实现RAG存储逻辑
        pass

    @property
    def memory(self) -> List[MemoryItem]:
        return self._memories

    def clear(self) -> None:
        self._memories.clear()

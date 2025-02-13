import asyncio
from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional, Dict, Any

from config.settings import MEMORY_SIZE
from agent.action import Action


@dataclass
class MemoryItem:
    user_input: str
    ai_response: str
    timestamp: datetime


class Memory:

    def __init__(self):
        self._memories: List[MemoryItem] = []

    async def add_memory(self, user_input: str, ai_response: str) -> None:
        memory_item = MemoryItem(user_input=user_input,
                                 ai_response=ai_response,
                                 timestamp=datetime.now())
        self._memories.append(memory_item)
        if len(self._memories) > MEMORY_SIZE:
            long_term_mem = self._memories[0]
            self._memories.pop(0)
            asyncio.create_task(self._save_to_rag(long_term_mem))

    async def _save_to_rag(self, memory_item: MemoryItem) -> None:
        # TODO
        pass

    @property
    def memory(self) -> List[MemoryItem]:
        return self._memories

    def clear(self) -> None:
        self._memories.clear()

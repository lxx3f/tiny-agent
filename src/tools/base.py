from typing import Any
from abc import ABC, abstractmethod


class Tool(ABC):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def run(self, **kwargs) -> Any:
        pass

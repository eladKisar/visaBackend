from abc import ABC, abstractmethod
from typing import List
from core import Form


class UserRepository(ABC):
    @abstractmethod
    async def register(self, username: str, password: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def login(self, username: str, password: str) -> bool:
        raise NotImplementedError


class FormRepository(ABC):
    @abstractmethod
    async def all(self) -> List[Form]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, content: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def read(self, form_id: str) -> Form:
        raise NotImplementedError

    @abstractmethod
    async def update(self, form_id: str, content: dict) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, form_id: str) -> bool:
        raise NotImplementedError

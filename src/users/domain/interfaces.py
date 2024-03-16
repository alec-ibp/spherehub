from abc import ABC, abstractmethod

from .models import User


class UserRegisterRepository(ABC):
    @abstractmethod
    async def register(self, user: User) -> User:
        raise NotImplementedError

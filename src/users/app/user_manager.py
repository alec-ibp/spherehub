from uuid import UUID

from ..domain.models import User, UserStatus
from ..domain.interfaces import UserRegisterRepository

from passlib.context import CryptContext


class UserRegister():
    def __init__(self, repository: UserRegisterRepository):
        self.repository: UserRegisterRepository = repository

    async def register(self, uid: UUID, name: str, lastname: str, email: str, password: str):
        hashed_password: str = CryptContext(schemes=["bcrypt"]).hash(password)
        new_user: User = User(
            uid=uid,
            name=name,
            lastname=lastname,
            email=email,
            password=hashed_password,
            status=UserStatus.REGISTERED.value
        )
        return await self.repository.register(new_user)

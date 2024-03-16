from src.users.domain.models import User
from src.users.domain.interfaces import UserRegisterRepository

from sqlalchemy.orm import Session


class UserRegisterService(UserRegisterRepository):
    def __init__(self, session: Session) -> None:
        self.session: Session = session

    async def register(self, user: User) -> User:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

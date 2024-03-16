from uuid import UUID
from enum import Enum


class UserStatus(Enum):
    ACTIVE: str = "active"
    INACTIVE: str = "inactive"
    BANED: str = "baned"
    REGISTERED: str = "registered"


class User():
    def __init__(
        self,
        uid: UUID,
        name: str,
        lastname: str,
        email: str,
        password: str,
        status: UserStatus = UserStatus.INACTIVE.value
    ):
        self.uid = uid
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.status = status

    @property
    def fullname(self) -> str:
        return f"{self.name} {self.lastname}"

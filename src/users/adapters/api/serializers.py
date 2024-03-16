from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

from src.users.domain.models import UserStatus


class BaseUserSerializer(BaseModel):
    uid: UUID
    name: str
    lastname: str
    email: EmailStr
    status: UserStatus


class UserRegisterSerializer(BaseModel):
    uid: UUID
    name: str = Field(str, min_length=2, max_length=50)
    lastname: str = Field(str, min_length=2, max_length=50)
    email: EmailStr
    password: str

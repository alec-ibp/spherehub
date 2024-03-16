from src.shared.adapters.db import Base

from src.users.domain.models import User, UserStatus

from sqlalchemy import Table, Column, String, UUID


domain_model: User = User

table_mapper: Table = Table(
    "users",
    Base().metadata,
    Column("uid", UUID, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("lastname", String(50), nullable=False),
    Column("email", String(255), nullable=False),
    Column("password", String, nullable=False),
    Column("status", String(50), nullable=False, default=UserStatus.INACTIVE.value),
)

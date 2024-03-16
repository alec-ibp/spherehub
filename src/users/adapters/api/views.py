from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from src.shared.adapters.db import get_db_session

from src.users.domain.models import User
from src.users.app.user_manager import UserRegister

from src.users.adapters.api.serializers import UserRegisterSerializer, BaseUserSerializer
from ..db.services import UserRegisterService


app_name: str = "Users API"
router: APIRouter = APIRouter()


@router.post(
    path="/registry/",
    status_code=status.HTTP_201_CREATED,
    response_model=BaseUserSerializer
)
async def registry_user(
    request_body: UserRegisterSerializer,
    session: AsyncSession = Depends(get_db_session)
) -> BaseUserSerializer:

    """ Register a new user. """

    user_repository: UserRegisterService = UserRegisterService(session=session)
    registered_user: User = await UserRegister(repository=user_repository).register(**request_body.model_dump())

    return registered_user

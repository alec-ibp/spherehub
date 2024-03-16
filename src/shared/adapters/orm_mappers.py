from typing import Final, Any
import importlib

from config import settings

from ..domain.exceptions import MissingDomainModelException, MissingTableMapperException

from sqlalchemy import Table
from sqlalchemy.orm import registry


MAPPER_REGISTRY: Final[registry] = registry()


def start_sqlalchemy_mappers() -> None:
    for _app in settings.INSTALLED_APPS:
        try:
            orm_mapper = importlib.import_module(f"src.{_app}.adapters.db.orm_mapper")
        except ModuleNotFoundError:
            continue

        if not hasattr(orm_mapper, "table_mapper"):
            raise MissingTableMapperException("Missing Model-Table Mapper")

        if not hasattr(orm_mapper, "domain_model"):
            raise MissingDomainModelException("Missing Domain Model specification")

        domain_model: Any = getattr(orm_mapper, "domain_model")
        table_mapper: Table = getattr(orm_mapper, "table_mapper")

        MAPPER_REGISTRY.map_imperatively(domain_model, table_mapper)

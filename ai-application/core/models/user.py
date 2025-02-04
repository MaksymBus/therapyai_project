from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from core.models.mixins.int_id_pk import IntIdPkMixin
from .base import Base


class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):
    pass
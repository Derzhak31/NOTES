from typing import Annotated, TYPE_CHECKING
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from core import Base, db_helper


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(SQLAlchemyBaseUserTable[int], Base):
    pass


async def get_user_db(
    session: Annotated["AsyncSession", Depends(db_helper.get_async_session)],
):
    yield SQLAlchemyUserDatabase(session, User)

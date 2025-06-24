from typing import Annotated, TYPE_CHECKING
from fastapi import Depends
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTable,
    SQLAlchemyAccessTokenDatabase,
)
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from core import Base, db_helper

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class AccessToken(SQLAlchemyBaseAccessTokenTable[int], Base):
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="cascade"), nullable=False
    )


async def get_access_token_db(
    session: Annotated["AsyncSession", Depends(db_helper.get_async_session)],
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)

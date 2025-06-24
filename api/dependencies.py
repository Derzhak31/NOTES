from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import Note
from core import db_helper
from api import crud


async def note_by_id(
    note_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Note:
    note = await crud.get_note(session=session, note_id=note_id)
    if note is not None:
        return note

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from api import crud
from api.schemas.notes import Note, NoteCreate, NoteUpdate
from api.dependencies import note_by_id


router = APIRouter(prefix="/notes", tags=["Записки"])


@router.get("/")
async def get_notes(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_notes(session=session)


@router.get("/{note_id}")
async def get_note(note: Note = Depends(note_by_id)):
    return note


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_note(
    note_in: NoteCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_note(session=session, note_in=note_in)


@router.patch("/{note_id}")
async def update_note(
    note_update: NoteUpdate,
    note: Note = Depends(note_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_note(session=session, note=note, note_update=note_update)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(
    note: Note = Depends(note_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_note(session=session, note=note)

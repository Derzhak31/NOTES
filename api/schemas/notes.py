# from datetime import UTC, datetime
# from typing import Optional
from pydantic import BaseModel, ConfigDict


class NoteBase(BaseModel):
    name: str
    context: str


class NoteCreate(NoteBase):
    pass
    # update_data: Optional[datetime]

    # def set_update_data(self) -> None:
    #     self.update_data = datetime.now(UTC)


class NoteUpdate(NoteCreate):
    name: str
    context: str


class Note(NoteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    # create_data: Optional[datetime]

    # def set_create_data(self) -> None:
    #     self.create_data = datetime.now(UTC)

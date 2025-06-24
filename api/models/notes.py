from sqlalchemy.orm import Mapped

from core import Base


class Note(Base):
    name: Mapped[str]
    context: Mapped[str]

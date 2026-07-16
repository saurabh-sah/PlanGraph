from __future__ import annotations 
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.mixins import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .thread import Thread
    from .user_memory import UserMemory
    from .document import Document

class User(
    Base,
    TimestampMixin
):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        nullable=False
    )

    threads: Mapped[list["Thread"]] = relationship(
        back_populates="user",
        cascade= "all, delete-orphan",
        passive_deletes= True
    )

    memories: Mapped[list["UserMemory"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    documents: Mapped[list["Document"]] = relationship(
        back_populates="user"
    )

# Thread is a class/dataType
# thread is an object of type User
# threads is the table name
# every row in table threads is an object of type Thread

# importing Thread in this file from .thread and importing User in .thread file from this file
# problem of circular imports (infinite loop)

# from __future__ import annotations 
# tells python "Don't evaluate type hints immediately. Treat them as strings until later."

# At runtime:
# TYPE_CHECKING == False
# so the import never happens, avoiding the circular import.
# But editors like VS Code pretend it's True while doing type analysis
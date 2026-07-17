from __future__ import annotations
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.mixins import TimestampMixin
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .message import Message
    from .thread_memory import ThreadMemory
    from .thread_summary import ThreadSummary
    from .document import Document

class Thread(
    Base,
    TimestampMixin
):
    __tablename__ = "threads"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        nullable=False
    )
    
    user_id : Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        index=True
    )

    user : Mapped["User"] = relationship(
        back_populates="threads",
        passive_deletes=True
    )

    messages: Mapped[list["Message"]] = relationship(
        back_populates="thread",
        foreign_keys="Message.thread_id",
        cascade="all, delete-orphan"
    )

    active_message_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "messages.id",
            ondelete="SET NULL"
        ),
        nullable=True,
        index=True
    )

    active_message: Mapped["Message | None"] = relationship(
        foreign_keys=[active_message_id],
        post_update=True
    )

    thread_memories: Mapped[list["ThreadMemory"]] = relationship(
        back_populates="thread",
        cascade="all, delete-orphan"
    )

    summary: Mapped["ThreadSummary | None"] = relationship(
        back_populates="thread",
        uselist=False,
        cascade="all, delete-orphan"
    )

    documents: Mapped[list["Document"]] = relationship(
        back_populates="thread"
    )

# User is a class/dataType
# user is an object of type User
# users is the table name
# user_id is the foreign key of table threads linked to table users col id
# every row in table users is an object of type User



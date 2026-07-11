from __future__ import annotations

from sqlalchemy import (
    ForeignKey,
    Enum,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base import Base
from app.models.mixins import TimestampMixin
from app.models.enums import MessageRole
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .thread import Thread

class Message(Base):

    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    thread_id: Mapped[int] = mapped_column(
        ForeignKey(
            "threads.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    parent_message_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "messages.id",
            ondelete="SET NULL"
        ),
        nullable=True,
        index=True
    )

    role: Mapped[MessageRole] = mapped_column(
        Enum(
            MessageRole,
            name="message_role"
        ),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        nullable=False
    )

    meta_data: Mapped[dict | None] = mapped_column(
        JSONB,
        name="metadata",
        nullable=True
    )

    created_at = TimestampMixin.created_at

    thread: Mapped["Thread"] = relationship(
        back_populates="messages",
        foreign_keys=[thread_id]
    )

    # Self Referential Relationships
    parent_message: Mapped["Message | None"] = relationship(
        back_populates="child_messages",
        remote_side=[id]
    )

    child_messages: Mapped[list["Message"]] = relationship(
        back_populates="parent_message"
    )
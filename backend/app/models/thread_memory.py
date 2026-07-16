from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Float,
    String
)

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from pgvector.sqlalchemy import Vector

from app.models.base import Base
from app.models.mixins import TimestampMixin
from app.models.enums import MemoryType

if TYPE_CHECKING:
    from .thread import Thread


class ThreadMemory(
    TimestampMixin,
    Base
):
    __tablename__ = "thread_memories"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    thread_id: Mapped[int] = mapped_column(
        ForeignKey(
            "threads.id",
            ondelete="CASCADE"
        ),
        index=True
    )

    memory_type: Mapped[MemoryType] = mapped_column(
        Enum(
            MemoryType,
            name="memory_type",
            values_callable=lambda x:
            [
                e.value
                for e in x
            ]
        ),
        nullable=False,
        index=True
    )

    content: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    importance: Mapped[float] = mapped_column(
        Float,
        nullable=False,
        default=0.5,
        server_default="0.5"
    )

    embedding: Mapped[list[float] | None] = mapped_column(
        Vector(3072),
        nullable=True
    )

    last_accessed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    meta_data: Mapped[dict | None] = mapped_column(
        JSONB,
        name="metadata",
        nullable=True
    )

    thread: Mapped["Thread"] = relationship(
        back_populates="thread_memories"
    )
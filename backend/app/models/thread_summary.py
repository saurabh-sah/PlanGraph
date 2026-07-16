from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.models.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from .thread import Thread


class ThreadSummary(
    TimestampMixin,
    Base
):

    __tablename__ = "thread_summaries"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    thread_id: Mapped[int] = mapped_column(
        ForeignKey(
            "threads.id",
            ondelete="CASCADE"
        ),
        unique=True,
        index=True
    )

    summary: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    thread: Mapped["Thread"] = relationship(
        back_populates="summary"
    )
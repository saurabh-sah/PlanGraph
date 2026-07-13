from __future__ import annotations
from datetime import datetime

from sqlalchemy import (
    Enum,
    ForeignKey,
    DateTime,
)

from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.models.base import Base
from app.models.mixins import TimestampMixin
from app.models.enums import AgentRunStatus
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .message import Message


class AgentRun(TimestampMixin, Base):

    __tablename__ = "agent_runs"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    trigger_message_id: Mapped[int] = mapped_column(
        ForeignKey(
            "messages.id",
            ondelete="CASCADE"
        ),
        index=True
    )

    response_message_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "messages.id",
            ondelete="SET NULL"
        ),
        nullable=True,
        index=True
    )

    status: Mapped[AgentRunStatus] = mapped_column(
        Enum(
            AgentRunStatus,
            name="agent_run_status",
            values_callable=lambda x: [e.value for e in x]
        ),
        default=AgentRunStatus.PENDING,
        server_default=AgentRunStatus.PENDING.value,
        nullable=False,
        index=True
    )

    error_message: Mapped[str | None]

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    meta_data: Mapped[dict | None] = mapped_column(
        JSONB,
        name="metadata",
        nullable=True
    )

    trigger_message: Mapped["Message"] = relationship(
        foreign_keys=[trigger_message_id],
        back_populates="triggered_runs"
    )

    response_message: Mapped["Message | None"] = relationship(
        foreign_keys=[response_message_id],
        back_populates="response_runs"
    )
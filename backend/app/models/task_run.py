from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey
)

from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.models.base import Base
from app.models.mixins import TimestampMixin

from app.models.enums import (
    ExecutionStatus
)

if TYPE_CHECKING:
    from .task import Task
    from .node_run import NodeRun


class TaskRun(
    TimestampMixin,
    Base
):

    __tablename__ = "task_runs"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    task_id: Mapped[int] = mapped_column(
        ForeignKey(
            "tasks.id",
            ondelete="CASCADE"
        ),
        index=True
    )

    status: Mapped[ExecutionStatus] = mapped_column(
        Enum(
            ExecutionStatus,
            name="execution_status",
            values_callable=lambda x:
            [
                e.value
                for e in x
            ]
        ),
        nullable=False,
        default=ExecutionStatus.PENDING,
        server_default="pending",
        index=True
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    output_data: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True
    )

    error_message: Mapped[str | None]

    attempt_number: Mapped[int] = mapped_column(
        default=1,
        nullable=False
    )

    meta_data: Mapped[dict | None] = mapped_column(
        JSONB,
        name="metadata",
        nullable=True
    )

    # ==========================
    # Relationships
    # ==========================

    task: Mapped["Task"] = relationship(
        back_populates="task_runs"
    )

    node_runs: Mapped[list["NodeRun"]] = relationship(
        back_populates="task_run",
        cascade="all, delete-orphan"
    )
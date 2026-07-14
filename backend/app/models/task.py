from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import (
    Enum,
    ForeignKey,
    String
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
    AgentType,
    TaskPriority,
    TaskStatus
)

if TYPE_CHECKING:
    from .agent_run import AgentRun
    from .task_run import TaskRun


class Task(
    TimestampMixin,
    Base
):

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    agent_run_id: Mapped[int] = mapped_column(
        ForeignKey(
            "agent_runs.id",
            ondelete="CASCADE"
        ),
        index=True
    )

    parent_task_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "tasks.id",
            ondelete="SET NULL"
        ),
        nullable=True,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    objective: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    agent_type: Mapped[AgentType] = mapped_column(
        Enum(
            AgentType,
            name="agent_type",
            values_callable=lambda x:
            [
                e.value
                for e in x
            ]
        ),
        nullable=False,
        index=True
    )

    status: Mapped[TaskStatus] = mapped_column(
        Enum(
            TaskStatus,
            name="task_status",
            values_callable=lambda x:
            [
                e.value
                for e in x
            ]
        ),
        nullable=False,
        default=TaskStatus.PENDING,
        server_default="pending",
        index=True
    )

    position: Mapped[int] = mapped_column(
        nullable=False,
        default=0
    )

    priority: Mapped[TaskPriority] = mapped_column(
        Enum(
            TaskPriority,
            name="task_priority",
            values_callable=lambda x:
            [
                e.value
                for e in x
            ]
        ),
        nullable=False,
        default=TaskPriority.MEDIUM,
        server_default="medium",
        index=True
    )

    depends_on: Mapped[list[int]] = mapped_column(
        JSONB,
        nullable=False,
        default=list
    )

    result: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True
    )

    error_message: Mapped[str | None] = mapped_column(
        nullable=True
    )

    is_terminal: Mapped[bool] = mapped_column(
        default=False,
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

    agent_run: Mapped["AgentRun"] = relationship(
        back_populates="tasks"
    )

    parent_task: Mapped["Task | None"] = relationship(
        back_populates="child_tasks",
        remote_side=[id]
    )

    child_tasks: Mapped[list["Task"]] = relationship(
        back_populates="parent_task"
    )

    task_runs: Mapped[list["TaskRun"]] = relationship(
        back_populates="task",
        cascade="all, delete-orphan"
    )
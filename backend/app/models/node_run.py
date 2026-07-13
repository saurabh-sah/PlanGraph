from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    DateTime,
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
    NodeRunStatus,
    NodeType
)

if TYPE_CHECKING:
    from .agent_run import AgentRun
    from .tool_call import ToolCall


class NodeRun(
    TimestampMixin,
    Base
):
    __tablename__ = "node_runs"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    agent_run_id: Mapped[int] = mapped_column(
        ForeignKey(
            "agent_runs.id",
            ondelete="CASCADE"
        ),
        index=True,
        nullable=False
    )

    parent_node_run_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "node_runs.id",
            ondelete="SET NULL"
        ),
        nullable=True,
        index=True
    )

    node_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True
    )

    node_type: Mapped[NodeType] = mapped_column(
        Enum(
            NodeType,
            name="node_type",
            values_callable=lambda x: [
                e.value
                for e in x
            ]
        ),
        nullable=False,
        index=True
    )

    status: Mapped[NodeRunStatus] = mapped_column(
        Enum(
            NodeRunStatus,
            name="node_run_status",
            values_callable=lambda x: [
                e.value
                for e in x
            ]
        ),
        default=NodeRunStatus.PENDING,
        server_default="pending",
        nullable=False,
        index=True
    )

    error_message: Mapped[str | None] = mapped_column(
        nullable=True
    )

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    input_data: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True
    )

    output_data: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True
    )

    meta_data: Mapped[dict | None] = mapped_column(
        JSONB,
        name="metadata",
        nullable=True
    )

    # ========================
    # Relationships
    # ========================

    agent_run: Mapped["AgentRun"] = relationship(
        back_populates="node_runs"
    )

    parent_node_run: Mapped["NodeRun | None"] = relationship(
        back_populates="child_node_runs",
        remote_side=[id],
        foreign_keys=[parent_node_run_id]
    )

    child_node_runs: Mapped[list["NodeRun"]] = relationship(
        back_populates="parent_node_run",
        foreign_keys=[parent_node_run_id]
    )

    tool_calls: Mapped[list["ToolCall"]] = relationship(
        back_populates="node_run",
        cascade="all, delete-orphan"
    )
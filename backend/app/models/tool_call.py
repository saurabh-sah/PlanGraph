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
from app.models.enums import ToolCallStatus


if TYPE_CHECKING:
    from .node_run import NodeRun


class ToolCall(
    TimestampMixin,
    Base
):
    __tablename__ = "tool_calls"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    # ==========================================
    # Parent Node
    # ==========================================

    node_run_id: Mapped[int] = mapped_column(
        ForeignKey(
            "node_runs.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    # ==========================================
    # Tool Information
    # ==========================================

    tool_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True
    )

    provider: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
        index=True
    )

    # OpenAI / Anthropic / LangGraph tool ids
    external_tool_call_id: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
        index=True
    )

    # ==========================================
    # Execution State
    # ==========================================

    status: Mapped[ToolCallStatus] = mapped_column(
        Enum(
            ToolCallStatus,
            name="tool_call_status",
            values_callable=lambda x: [
                e.value
                for e in x
            ]
        ),
        nullable=False,
        default=ToolCallStatus.PENDING,
        server_default="pending",
        index=True
    )

    error_message: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    # ==========================================
    # Timing
    # ==========================================

    started_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    # ==========================================
    # Tool Inputs / Outputs
    # ==========================================

    arguments: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True
    )

    result: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True
    )

    # ==========================================
    # Extra Observability Metadata
    # ==========================================

    meta_data: Mapped[dict | None] = mapped_column(
        JSONB,
        name="metadata",
        nullable=True
    )

    # ==========================================
    # Relationships
    # ==========================================

    node_run: Mapped["NodeRun"] = relationship(
        back_populates="tool_calls"
    )
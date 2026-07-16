from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import (
    Enum,
    ForeignKey,
    String,
    BigInteger
)

from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.models.base import Base
from app.models.mixins import TimestampMixin
from app.models.enums import DocumentStatus

if TYPE_CHECKING:
    from .user import User
    from .thread import Thread
    from .document_chunk import DocumentChunk


class Document(
    TimestampMixin,
    Base
):

    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        nullable=True,
        index=True
    )

    thread_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "threads.id",
            ondelete="CASCADE"
        ),
        nullable=True,
        index=True
    )

    filename: Mapped[str] = mapped_column(
        nullable=False
    )

    title: Mapped[str | None]

    summary: Mapped[str | None]

    mime_type: Mapped[str] = mapped_column(
        nullable=False
    )

    size: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False
    )

    storage_path: Mapped[str] = mapped_column(
        nullable=False
    )

    status: Mapped[DocumentStatus] = mapped_column(
        Enum(
            DocumentStatus,
            name="document_status",
            values_callable=lambda x:
            [
                e.value
                for e in x
            ]
        ),
        nullable=False,
        default=DocumentStatus.UPLOADING,
        server_default="uploading",
        index=True
    )

    meta_data: Mapped[dict | None] = mapped_column(
        JSONB,
        name="metadata",
        nullable=True
    )

    user: Mapped["User | None"] = relationship(
        back_populates="documents"
    )

    thread: Mapped["Thread | None"] = relationship(
        back_populates="documents"
    )

    chunks: Mapped[list["DocumentChunk"]] = relationship(
        back_populates="document",
        cascade="all, delete-orphan"
    )
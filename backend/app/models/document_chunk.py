from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    Integer,
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

if TYPE_CHECKING:
    from .document import Document


class DocumentChunk(
    Base
):

    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    document_id: Mapped[int] = mapped_column(
        ForeignKey(
            "documents.id",
            ondelete="CASCADE"
        ),
        index=True
    )

    parent_chunk_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "document_chunks.id",
            ondelete="SET NULL"
        ),
        nullable=True,
        index=True
    )

    chunk_index: Mapped[int] = mapped_column(
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    token_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    embedding: Mapped[list[float] | None] = mapped_column(
        Vector(3072),
        nullable=True
    )

    meta_data: Mapped[dict | None] = mapped_column(
        JSONB,
        name="metadata",
        nullable=True
    )

    document: Mapped["Document"] = relationship(
        back_populates="chunks"
    )

    parent_chunk: Mapped["DocumentChunk | None"] = relationship(
        back_populates="child_chunks",
        remote_side=[id]
    )

    child_chunks: Mapped[list["DocumentChunk"]] = relationship(
        back_populates="parent_chunk"
    )
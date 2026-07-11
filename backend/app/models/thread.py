from __future__ import annotations
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.mixins import TimestampMixin
from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class Thread(
    Base,
    TimestampMixin
):
    __tablename__ = "threads"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        nullable=False
    )
    
    user_id : Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True
    )

    user : Mapped["User"] = relationship(
        back_populates="threads",
        cascade= "all, delete-orphan",
        passive_deletes=True
    )

# User is a class/dataType
# user is an object of type User
# users is the table name
# user_id is the foreign key of table threads linked to table users col id
# every row in table users is an object of type User



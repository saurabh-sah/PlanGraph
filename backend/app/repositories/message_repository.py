from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from app.models.message import Message


def get_message(
    db: Session,
    message_id: int
) -> Message | None:

    stmt = (
        select(Message)
        .where(
            Message.id == message_id
        )
    )

    return db.execute(
        stmt
    ).scalar_one_or_none()


def get_thread_messages(
    db: Session,
    thread_id: int
):

    stmt = (
        select(Message)
        .where(
            Message.thread_id == thread_id
        )
        .order_by(
            Message.created_at
        )
    )

    return (
        db.execute(stmt)
        .scalars()
        .all()
    )
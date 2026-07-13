from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from app.models.thread import Thread
from app.schemas.thread import ThreadQuery


def get_thread(
    db: Session,
    thread_id: int
) -> Thread | None:

    stmt = (
        select(Thread)
        .where(
            Thread.id == thread_id
        )
    )

    return db.execute(
        stmt
    ).scalar_one_or_none()


def get_thread_with_head(
    db: Session,
    thread_id: int
):

    stmt = (
        select(Thread)
        .options(
            selectinload(
                Thread.active_message
            )
        )
        .where(
            Thread.id == thread_id
        )
    )

    return db.execute(
        stmt
    ).scalar_one_or_none()


def list_all_threads(
    db: Session,
    user_id: int
):

    stmt = (
        select(Thread)
        .where(
            Thread.user_id == user_id
        )
    )

    return (
        db.execute(stmt)
        .scalars()
        .all()
    )

def list_threads(
    db: Session,
    user_id: int,
    thread_info: ThreadQuery
) -> list[Thread]:

    stmt = (
        select(Thread)
        .where(
            Thread.user_id == user_id
        )
        .options(
            selectinload(Thread.user)
        )
        .order_by(
            Thread.updated_at.desc()
        )
        .limit(thread_info.limit)
        .offset(thread_info.offset)
    )

    threads = (
        db.execute(stmt)
        .scalars()
        .all()
    )

    return threads


def get_thread_with_user(
    db: Session,
    thread_id: int
) -> Thread | None:

    stmt = (
        select(Thread)
        .where(Thread.id == thread_id)
        .options(
            selectinload(Thread.user)
        )
    )

    thread = (
        db.execute(stmt)
        .scalar_one_or_none()
    )

    return thread
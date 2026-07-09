from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.thread import Thread
from app.schemas import ThreadCreateRequest, ThreadQuery   # <-- later we'll move schemas


def create_thread(
    db: Session,
    thread_info: ThreadCreateRequest,
) -> Thread:

    thread = Thread(
        title=thread_info.title,
        user_id=thread_info.user_id,
    )

    db.add(thread)

    db.commit()

    db.refresh(thread)

    return thread

def list_threads(
        db: Session,
        thread_info: ThreadQuery
) -> list[Thread]:
    
    stmt = (
        select(Thread)
        .limit(thread_info.limit)
        .offset(thread_info.offset)
    )

    threads = db.execute(stmt).scalars().all()

    return threads

def get_thread(
    db: Session,
    thread_id: int,
) -> Thread | None:

    stmt = (
        select(Thread)
        .where(Thread.id == thread_id)
    )

    thread = db.execute(stmt).scalar_one_or_none()

    return thread
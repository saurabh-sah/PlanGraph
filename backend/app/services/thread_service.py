from sqlalchemy.orm import Session

from app.models.thread import Thread
from app.schemas import ThreadCreateRequest   # <-- later we'll move schemas


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
from app.models.thread import Thread
from sqlalchemy.orm import Session
from pydantic import BaseModel

class ThreadCreateDTO(BaseModel):
    title: str
    user_id: int

def create_thread(
    db: Session,
    thread_info: ThreadCreateDTO
) -> Thread:
    
    thread = Thread(
        title = thread_info.title,
        user_id = thread_info.user_id
    )

    db.add(thread)

    db.flush()

    db.commit()

    db.refresh(thread)

    return thread
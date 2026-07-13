from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select

from app.models.thread import Thread
from app.schemas import ThreadCreateRequest, ThreadUpdateRequest   # <-- later we'll move schemas
from app.repositories.thread_repository import get_thread


def create_thread(
    db: Session,
    thread_info: ThreadCreateRequest,
) -> Thread:

    try:
        thread = Thread(
            title=thread_info.title,
            user_id=thread_info.user_id,
        )

        db.add(thread)

        db.commit()

        db.refresh(thread)

        return thread
    
    except:
        db.rollback()
        raise


def update_thread(
        db: Session,
        thread_id: int,
        updated_thread: ThreadUpdateRequest
) -> Thread | None:
    
    try:
        curr_thread = get_thread(
            db=db,
            thread_id=thread_id
        ) # persistant obj

        if curr_thread is None:
            return None 

        curr_thread.title = updated_thread.title # dirty tracking

        db.commit()

        db.refresh(curr_thread)

        return curr_thread
    
    except:
        db.rollback()
        raise


def delete_thread(
        db: Session,
        thread_id: int
) -> bool:
    
    try:
        thread = get_thread(
            db=db,
            thread_id=thread_id
        ) # persistant obj

        if thread is None:
            return False
        
        db.delete(thread)

        db.commit()

        return True
    
    except:
        db.rollback()
        raise

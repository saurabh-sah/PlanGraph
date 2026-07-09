from fastapi import APIRouter, HTTPException, Depends
from app.schemas.thread import ThreadCreateRequest, ThreadQuery, ThreadResponse

from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.services.thread_service import create_thread
from services.thread_service import list_threads

router = APIRouter(
    prefix="/threads",
    tags=["Threads"]
)


@router.get("/threads", response_model=list[ThreadResponse])
def get_threads(
    thread_info: ThreadQuery = Depends(),
    db: Session = Depends(get_db)
):
    threads = list_threads(db=db, thread_info=thread_info)

    return [
        ThreadResponse(
            id=thread.id,
            title=thread.title,
            user_id=thread.user_id
        ) for thread in threads
    ]


@router.post("/threads", response_model=ThreadResponse)
def create_thread_route(
    thread_info: ThreadCreateRequest,
    db: Session = Depends(get_db),
):
    thread = create_thread(
        db=db,
        thread_info=thread_info,
    )

    return ThreadResponse(
        id=thread.id,
        title=thread.title,
        user_id=thread.user_id,
    )
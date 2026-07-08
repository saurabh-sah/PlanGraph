from fastapi import APIRouter, HTTPException, Depends
from app.schemas.thread import ThreadCreateRequest, ThreadQuery, ThreadResponse

from sqlalchemy.orm import Session

from backend.app.db.session import get_db
from backend.app.services.thread_service import create_thread

router = APIRouter(
    prefix="/threads",
    tags=["Threads"]
)

# -----------------------------
# Temporary Fake Data
# -----------------------------

fake_threads = {
    1: "LangGraph discussion",
    2: "FastAPI notes",
    3: "RAG ideas",
}


@router.get("/threads", response_model=list[ThreadResponse])
def get_threads(thread_info: ThreadQuery = Depends()):
    response = []

    remaining = thread_info.limit
    skip = thread_info.offset

    for thread_id, title in fake_threads.items():

        if skip > 0:
            skip -= 1
            continue

        if remaining == 0:
            break

        response.append(
            ThreadResponse(
                id=thread_id,
                title=title,
                user_id=1,  # Temporary until DB-backed
            )
        )

        remaining -= 1

    if not response:
        raise HTTPException(
            status_code=404,
            detail="Threads Not Found",
        )

    return response


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
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.thread import ThreadCreateRequest, ThreadQuery, ThreadResponse, ThreadUpdateRequest, DeleteThreadResponse

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.thread_service import create_thread, update_thread, delete_thread
from app.repositories.thread_repository import list_threads
from app.repositories.thread_repository import get_thread_with_user
from app.core.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/threads",
    tags=["Threads"]
)


@router.get("/",response_model=list[ThreadResponse])
def get_threads(
    current_user: User = Depends(
        get_current_user
    ),
    thread_info: ThreadQuery = Depends(),
    db: Session = Depends(get_db)
):

    threads = list_threads(
        db=db,
        user_id=current_user.id,
        thread_info=thread_info
    )

    return [
        ThreadResponse.model_validate(
            thread
        )
        for thread in threads
    ]


@router.post("/", response_model=ThreadResponse)
def create_thread_route(
    thread_info: ThreadCreateRequest,
    db: Session = Depends(get_db),
):
    thread = create_thread(
        db=db,
        thread_info=thread_info,
    )

    return ThreadResponse.model_validate(
        thread
    )

@router.get("/{thread_id}",response_model=ThreadResponse)
def get_thread_route(
    thread_id: int,
    db: Session = Depends(get_db)
):

    thread = get_thread_with_user(
        db=db,
        thread_id=thread_id
    )

    if thread is None:
        raise HTTPException(
            status_code=404,
            detail="Thread not found"
        )

    return ThreadResponse.model_validate(
        thread
    )

@router.patch("/{thread_id}", response_model=ThreadResponse)
def update_thread_route(
    thread_id: int,
    updated_thread: ThreadUpdateRequest,
    db: Session = Depends(get_db),
):
    thread = update_thread(
        db=db,
        thread_id=thread_id,
        updated_thread=updated_thread
    )

    if thread is None:
        raise HTTPException(
            status_code=404,
            detail="Thread not found"
        )

    return ThreadResponse.model_validate(
        thread
    )

@router.delete("/{thread_id}")
def delete_thread_route(
    thread_id: int,
    db: Session = Depends(get_db)
):
    
    deleted = delete_thread(
        db=db,
        thread_id=thread_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Thread not found"
        )
        
    return DeleteThreadResponse(
        success=True,
        message="Thread deleted."
    )
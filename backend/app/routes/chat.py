from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.graph.builder import (
    get_graph
)

from app.schemas.chat import (
    ChatRequest,
    ChatResponse
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "/",
    response_model=ChatResponse
)
def chat_response(
    request: ChatRequest
):

    db: Session = SessionLocal()

    try:

        graph = get_graph()

        result = graph.invoke(

            {

                "user_id": 1,

                "thread_id":
                    request.thread_id,

                "trigger_message_id": 1,

                "agent_run_id": 1,
            },

            config={

                "configurable": {

                    "db": db
                }
            }
        )

        return ChatResponse(

            answer=str(result),

            model="runtime-test",

            success=True,
        )

    finally:

        db.close()
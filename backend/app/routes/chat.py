from fastapi import (
    APIRouter,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.session import sessionLocal

from app.graph.builder import (
    get_graph
)

from app.schemas.chat import (
    ChatRequest,
    ChatResponse
)

from app.repositories.thread_repository import (
    get_thread_with_head
)

from app.services.message_service import (
    create_human_message,
    create_ai_message
)

from app.services.agent_run_service import (
    create_agent_run,
    start_agent_run,
    complete_agent_run,
    fail_agent_run
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

    db: Session = sessionLocal()

    try:

        thread = get_thread_with_head(
            db,
            request.thread_id
        )

        if thread is None:

            raise HTTPException(
                status_code=404,
                detail="Thread not found."
            )

        human_message = (
            create_human_message(
                db=db,
                thread=thread,
                content=request.message
            )
        )

        run = create_agent_run(
            db=db,
            trigger_message=human_message
        )

        start_agent_run(run)

        db.commit()

        db.refresh(run)

        graph = get_graph()

        result = graph.invoke(

            {

                "user_id":
                    thread.user_id,

                "thread_id":
                    thread.id,

                "trigger_message_id":
                    human_message.id,

                "agent_run_id":
                    run.id,
            },

            config={

                "configurable": {

                    "db": db
                }
            }
        )

        answer = (
            result.get(
                "final_response"
            )
            or "No response generated."
        )

        ai_message = (
            create_ai_message(

                db=db,

                thread=thread,

                content=answer,

                triggering_message=
                    human_message
            )
        )

        complete_agent_run(
            run,
            ai_message
        )

        db.flush()
        
        db.commit()

        return ChatResponse(

            answer=answer,

            model="plangraph",

            success=True,
        )

    except Exception as e:

        db.rollback()

        if (
            "run" in locals()
            and run is not None
        ):

            fail_agent_run(
                run,
                str(e)
            )

            db.commit()

        raise

    finally:

        db.close()
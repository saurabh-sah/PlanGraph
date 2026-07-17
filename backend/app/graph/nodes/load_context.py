from langchain_core.runnables import (
    RunnableConfig
)

from app.core.config import settings

from app.graph.state import (
    GraphState
)

from app.graph.mappers.message_mapper import (
    to_chat_history
)

from app.repositories import (
    thread_repository
)

from app.services.message_service import (
    get_active_conversation
)


def load_context_node(
    state: GraphState,
    config: RunnableConfig,
):

    db = config["configurable"]["db"]

    thread = (
        thread_repository
        .get_thread_with_head(
            db,
            state["thread_id"]
        )
    )

    # if not thread:

    #     raise ValueError(
    #         f"Thread "
    #         f"{state['thread_id']} "
    #         f"not found"
    #     )

    if thread is None:
        return {
            "messages": [],
            "planner_context": None
        }

    messages = (
        get_active_conversation(
            thread
        )
    )

    messages = messages[
        -settings.graph_context_window:
    ]

    chat_history = (
        to_chat_history(
            messages
        )
    )

    return {

        "messages":
            chat_history
    }
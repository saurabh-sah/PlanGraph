from app.graph.state import GraphState
from app.models.enums import AgentType

from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

from app.graph.state import (
    GraphState
)

from app.graph.planner.schemas import (
    PlannerOutput
)

from app.graph.planner.prompts import (
    PLANNER_SYSTEM_PROMPT
)

from app.core.llm_factory import (
    create_llm
)

from app.graph.planner.schemas import (
    PlannerOutput,
    TaskSpec
)


def planner_node(
    state: GraphState,
):

    messages = state.get(
        "messages",
        []
    )

    planner_context = state.get(
        "planner_context",
        ""
    )

    llm = create_llm()

    structured_llm = (
        llm.with_structured_output(
            PlannerOutput
        )
    )

    history = "\n".join(
        [
            f"{m.type}: {m.content}"
            for m in messages
        ]
    )

    if not history:

        history = (
            "User: Hello"
        )
        

    user_prompt = f"""
Conversation:

{history}


Retrieved Context:

{planner_context}
"""

    output = structured_llm.invoke(

        [

            SystemMessage(
                content=
                    PLANNER_SYSTEM_PROMPT
            ),

            HumanMessage(
                content=user_prompt
            )
        ]
    )

    return {

        "planner_output":
            output
    }
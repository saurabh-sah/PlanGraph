from typing import TypedDict

from langchain_core.messages import BaseMessage

from app.graph.planner.schemas import (
    PlannerOutput
)


class GraphState(
    TypedDict,
    total=False
):

    # identifiers

    user_id: int
    thread_id: int
    trigger_message_id: int
    agent_run_id: int
    llm_provider: str | None
    llm_model: str | None

    # conversation

    messages: list[BaseMessage]

    # retrieval

    retrieved_memories: list[dict]

    retrieved_documents: list[dict]

    planner_context: str | None

    # planning

    planner_output: PlannerOutput | None

    # execution

    ready_task_run_ids: list[int]

    completed_task_run_ids: set[int]

    failed_task_run_ids: set[int]

    task_results: dict[int, dict]

    # final response

    final_response: str | None
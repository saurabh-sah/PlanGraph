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

    # runtime messages

    messages: list[BaseMessage]

    # planner

    planner_output: PlannerOutput | None

    # execution

    ready_task_run_ids: list[int]

    completed_task_ids: set[int]

    failed_task_ids: set[int]

    task_results: dict[int, dict]

    # final output

    final_response: str | None
from app.graph.state import GraphState

from app.services.executor_service import (
    execute_task_run
)


def executor_node(
    state: GraphState,
    config,
):
    db = config["configurable"]["db"]

    ready = state.get(
        "ready_task_run_ids",
        []
    )

    if not ready:
        return {}

    task_results = {}

    completed = set()

    for task_run_id in ready:

        result = execute_task_run(
            db=db,
            task_run_id=task_run_id
        )

        task_results[
            task_run_id
        ] = result

        completed.add(
            task_run_id
        )

    db.commit()

    return {

        "task_results":
            task_results,

        "completed_task_run_ids":
            completed,

        "ready_task_run_ids":
            []
    }
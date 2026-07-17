from app.graph.state import GraphState


def executor_node(
    state: GraphState,
):

    return {

        "task_results": {},

        "completed_task_ids": set(),

        "failed_task_ids": set(),
    }
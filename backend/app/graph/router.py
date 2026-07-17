from app.graph.state import GraphState


def route_after_scheduler(
    state: GraphState
):

    ready = state.get(
        "ready_task_run_ids",
        []
    )

    if ready:

        return "executor"

    return "synthesizer"
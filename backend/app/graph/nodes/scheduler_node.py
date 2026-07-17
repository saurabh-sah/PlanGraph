from app.graph.state import GraphState


def scheduler_node(
    state: GraphState,
):

    print("scheduler called")
    
    return {
        "ready_task_run_ids":
            state.get(
                "ready_task_run_ids",
                []
            )
    }
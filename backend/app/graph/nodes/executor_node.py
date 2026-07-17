from app.graph.state import GraphState


def executor_node(
    state: GraphState,
):

    print("executor called")
    print(state)
    
    ready = state.get(
        "ready_task_run_ids",
        []
    )

    if not ready:

        return {}

    executed = ready[0]

    return {

        "task_results": {

            executed: {

                "response":
                    "Hello from executor."
            }
        },

        "completed_task_run_ids": {
            executed
        },

        "ready_task_run_ids": []
    }
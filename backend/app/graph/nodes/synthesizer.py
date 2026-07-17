from app.graph.state import GraphState


def synthesizer_node(
    state: GraphState,
):

    results = state.get(
        "task_results",
        {}
    )

    return {

        "final_response":
            str(results)
    }
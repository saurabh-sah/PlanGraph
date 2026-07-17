from app.graph.state import GraphState
from app.core.llm_factory import create_llm


def synthesizer_node(
    state: GraphState,
):
    task_results = state.get(
        "task_results",
        {}
    )

    if not task_results:
        return {
            "final_response":
                "No response generated."
        }

    llm = create_llm()

    response = llm.invoke(
        f"""
You are a synthesis agent.

Combine the following task outputs
into the final response for the user.

Task Outputs:

{task_results}
"""
    )

    return {
        "final_response":
            response.content
    }
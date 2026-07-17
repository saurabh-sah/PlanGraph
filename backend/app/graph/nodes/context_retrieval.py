from app.graph.state import GraphState


def context_retrieval_node(
    state: GraphState,
):

    sections = []

    sections.append(
        "=== THREAD SUMMARY ===\n\n"
        "No summary available.".strip()
    )


    sections.append(
        "=== RELEVANT MEMORIES ===\n\n"
        "No relevant memories retrieved.".strip()
    )

    sections.append(
        "=== RELEVANT DOCUMENTS ===\n\n"
        "No relevant documents retrieved.".strip()
    )

    planner_context = "\n\n".join(
        sections
    )

    return {

        "retrieved_memories": [],

        "retrieved_documents": [],

        "planner_context":
            planner_context
    }
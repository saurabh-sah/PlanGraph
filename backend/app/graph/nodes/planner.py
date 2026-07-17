from app.graph.state import GraphState

from app.graph.planner.schemas import (
    PlannerOutput
)


def planner_node(
    state: GraphState,
):

    plan = PlannerOutput(
        tasks=[],
        reasoning="Runtime skeleton planner.",
    )

    return {
        "planner_output": plan
    }
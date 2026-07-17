from app.graph.state import GraphState
from app.graph.planner.schemas import (
    PlannerOutput
)


def planner_node(
    state: GraphState
):

    # TODO:
    # fetch context

    # TODO:
    # call llm

    plan = PlannerOutput(
        tasks=[]
    )

    return {
        "planner_output": plan
    }
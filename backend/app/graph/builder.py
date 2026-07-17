from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.graph.state import GraphState

from app.graph.nodes.load_context import (
    load_context_node
)

from app.graph.nodes.context_retrieval import (
    context_retrieval_node
)

from app.graph.nodes.planner import (
    planner_node
)

from app.graph.nodes.persist_plan import (
    persist_plan_node
)

from app.graph.nodes.scheduler_node import (
    scheduler_node
)

from app.graph.nodes.executor_node import (
    executor_node
)

from app.graph.nodes.synthesizer import (
    synthesizer_node
)

from app.graph.router import (
    route_after_scheduler
)

from functools import lru_cache

@lru_cache
def get_graph():

    return build_graph()


def build_graph():

    graph = StateGraph(
        GraphState
    )

    graph.add_node(
        "load_context",
        load_context_node
    )

    graph.add_node(
        "context_retrieval",
        context_retrieval_node
    )

    graph.add_node(
        "planner",
        planner_node
    )

    graph.add_node(
        "persist_plan",
        persist_plan_node
    )

    graph.add_node(
        "scheduler",
        scheduler_node
    )

    graph.add_node(
        "executor",
        executor_node
    )

    graph.add_node(
        "synthesizer",
        synthesizer_node
    )

    graph.add_edge(
        START,
        "load_context"
    )

    graph.add_edge(
        "load_context",
        "context_retrieval"
    )

    graph.add_edge(
        "context_retrieval",
        "planner"
    )

    graph.add_edge(
        "planner",
        "persist_plan"
    )

    graph.add_edge(
        "persist_plan",
        "scheduler"
    )

    graph.add_conditional_edges(
        "scheduler",
        route_after_scheduler,
        {
            "executor": "executor",
            "synthesizer": "synthesizer"
        }
    )

    graph.add_edge(
        "executor",
        "scheduler"
    )

    graph.add_edge(
        "synthesizer",
        END
    )

    return graph.compile()
from graph.planner.schemas import (
    PlannerOutput,
    TaskSpec
)


def get_ready_tasks(
    plan: PlannerOutput,
    completed: set[int]
):

    ready = []

    for task in plan.tasks:

        if task.id in completed:
            continue

        if all(
            dep in completed
            for dep in task.depends_on
        ):
            ready.append(task)

    return ready
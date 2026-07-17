from app.models.task import Task
from app.models.enums import (
    TaskStatus,
    TaskPriority
)


def persist_plan(
    db,
    agent_run,
    plan
):

    tasks = []

    for position, spec in enumerate(
        plan.tasks
    ):

        task = Task(

            agent_run=agent_run,

            title=spec.title,

            objective=spec.objective,

            agent_type=spec.agent_type,

            status=TaskStatus.PENDING,

            priority=TaskPriority(
                spec.priority
            ),

            depends_on=spec.depends_on,

            position=position,

            is_terminal=spec.is_terminal
        )

        db.add(task)

        tasks.append(task)

    db.flush()

    return tasks
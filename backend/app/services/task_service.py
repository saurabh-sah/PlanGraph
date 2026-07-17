from app.models.task import Task
from app.models.task_run import TaskRun
from app.models.enums import (
    TaskStatus,
    TaskPriority, 
    ExecutionStatus
)


def persist_plan(
    db,
    agent_run_id: int,
    plan
):

    tasks = []
    task_runs = []

    for position, spec in enumerate(plan.tasks):

        task = Task(

            agent_run_id=agent_run_id,

            title=spec.title,

            objective=spec.objective,

            agent_type=spec.agent_type,

            status=TaskStatus.PENDING,

            priority=TaskPriority(
                spec.priority
            ),

            depends_on=spec.depends_on,

            position=position,

            is_terminal=spec.is_terminal,
        )

        db.add(task)

        tasks.append(task)

    db.flush()

    for task in tasks:

        task_run = TaskRun(

            task_id=task.id,

            status=ExecutionStatus.PENDING,

            attempt_number=1,
        )

        db.add(task_run)

        task_runs.append(task_run)

    db.flush()

    return tasks, task_runs
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.task_run import TaskRun
from app.models.enums import (
    ExecutionStatus,
    TaskStatus
)

from app.core.llm_factory import create_llm


def execute_task_run(
    db: Session,
    task_run_id: int,
):
    task_run = db.get(
        TaskRun,
        task_run_id
    )

    if task_run is None:
        raise ValueError(
            f"TaskRun {task_run_id} not found."
        )

    task = task_run.task

    # mark running
    task_run.status = (
        ExecutionStatus.RUNNING
    )

    task.status = TaskStatus.RUNNING

    task_run.started_at = (
        datetime.now(timezone.utc)
    )

    db.flush()

    llm = create_llm()

    response = llm.invoke(
        f"""
You are an execution agent.

Task Title:
{task.title}

Task Objective:
{task.objective}

Return only the result.
"""
    )

    result = {
        "response": response.content
    }

    task_run.output_data = result
    task_run.status = (
        ExecutionStatus.COMPLETED
    )

    task_run.completed_at = (
        datetime.now(timezone.utc)
    )

    task.result = result
    task.status = (
        TaskStatus.COMPLETED
    )

    db.flush()

    return result
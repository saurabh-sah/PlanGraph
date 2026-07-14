from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.agent_run import AgentRun
from app.models.enums import ExecutionStatus
from app.models.message import Message


def create_agent_run(
    db: Session,
    trigger_message: Message
) -> AgentRun:

    run = AgentRun(
        trigger_message=trigger_message,
        status=ExecutionStatus.PENDING
    )

    db.add(run)

    db.flush()

    return run


def start_agent_run(
    run: AgentRun
) -> None:

    run.status = ExecutionStatus.RUNNING

    run.started_at = datetime.now(
        timezone.utc
    )


def complete_agent_run(
    run: AgentRun,
    response_message: Message
) -> None:

    run.status = ExecutionStatus.COMPLETED

    run.response_message = response_message

    run.completed_at = datetime.now(
        timezone.utc
    )


def fail_agent_run(
    run: AgentRun,
    error_message: str | None = None
):

    run.status = ExecutionStatus.FAILED

    run.error_message = error_message

    run.completed_at = datetime.now(
        timezone.utc
    )

def interrupt_agent_run(
    run: AgentRun
) -> None:

    run.status = ExecutionStatus.INTERRUPTED

    run.completed_at = datetime.now(
        timezone.utc
    )


def cancel_agent_run(
    run: AgentRun
) -> None:

    run.status = ExecutionStatus.CANCELLED

    run.completed_at = datetime.now(
        timezone.utc
    )
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.agent_run import AgentRun

def get_agent_run(
    db: Session,
    run_id: int
):

    stmt = (
        select(AgentRun)
        .where(
            AgentRun.id == run_id
        )
    )

    return db.execute(
        stmt
    ).scalar_one_or_none()
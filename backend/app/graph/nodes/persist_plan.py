from app.services.task_service import (
    persist_plan
)


def persist_plan_node(
    state,
    config,
):

    db = config["configurable"]["db"]

    _, task_runs = persist_plan(

        db=db,

        agent_run_id=state["agent_run_id"],

        plan=state["planner_output"],
    )

    db.commit()

    return {

        "ready_task_run_ids": [
            tr.id
            for tr in task_runs
        ]
    }
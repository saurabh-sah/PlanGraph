# scripts/test_graph.py

from app.graph.builder import (
    get_graph
)

from app.db.session import (
    sessionLocal
)

from app.models.message import Message

from app.services.agent_run_service import (
    create_agent_run,
    start_agent_run
)


def main():

    graph = get_graph()

    db = sessionLocal()

    message = db.get(
        Message,
        1
    )

    run = create_agent_run(
        db=db,
        trigger_message=message
    )

    start_agent_run(run)

    db.commit()

    db.refresh(run)

    try:

        result = graph.invoke(

            {

                "user_id": 1,

                "thread_id": 4,

                "trigger_message_id": message.id,

                "agent_run_id": run.id,
            },

            config={
                "configurable": {
                    "db": db
                }
            }
        )

        print()

        print("=" * 80)

        print(result)

        print("=" * 80)

    finally:

        db.close()


if __name__ == "__main__":

    main()
# scripts/test_graph.py

from app.graph.builder import (
    get_graph
)

from app.db.session import (
    sessionLocal
)


def main():

    graph = get_graph()

    db = sessionLocal()

    try:

        result = graph.invoke(

            {

                "user_id": 1,

                "thread_id": 1,

                "trigger_message_id": 1,

                "agent_run_id": 1,
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
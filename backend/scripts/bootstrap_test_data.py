from app.db.session import sessionLocal

from app.models.user import User
from app.models.thread import Thread
from app.models.message import Message

from app.models.enums import MessageRole


def main():

    db = sessionLocal()

    try:

        # cleanup for repeated runs
        db.query(Message).delete()
        db.query(Thread).delete()
        db.query(User).delete()

        db.commit()

        user = User(
            name="Test User"
        )

        db.add(user)
        db.flush()

        thread = Thread(
            title="Test Thread",
            user=user
        )

        db.add(thread)
        db.flush()

        message = Message(
            thread=thread,
            role=MessageRole.HUMAN,
            content="Hello"
        )

        db.add(message)
        db.flush()

        thread.active_message = message

        db.commit()

        print()

        print("=" * 80)

        print(f"user_id = {user.id}")
        print(f"thread_id = {thread.id}")
        print(f"message_id = {message.id}")

        print("=" * 80)

    finally:
        db.close()


if __name__ == "__main__":
    main()
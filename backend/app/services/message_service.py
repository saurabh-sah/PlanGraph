from sqlalchemy.orm import Session
from app.models.thread import Thread
from app.models.message import Message
from app.models.enums import MessageRole

def create_message(
    db: Session,
    thread: Thread,
    role: MessageRole,
    content: str,
    parent_message: Message | None
) -> Message:

    message = Message(
        thread=thread,
        role=role,
        content=content,
        parent_message=parent_message
    )

    db.add(message)

    db.flush()

    return message


def get_active_conversation(
    thread: Thread
) -> list[Message]:
    
    curr = thread.active_message

    messages = []

    while curr:
        messages.append(curr)
        curr = curr.parent_message

    messages.reverse()

    return messages

def create_human_message(
    db: Session,
    thread: Thread,
    content: str
):

    parent = thread.active_message

    message = create_message(
        db=db,
        thread=thread,
        role=MessageRole.HUMAN,
        content=content,
        parent_message=parent
    )

    thread.active_message = message

    return message

def create_ai_message(
    db: Session,
    thread: Thread,
    content: str,
    triggering_message: Message
):

    message = create_message(
        db=db,
        thread=thread,
        role=MessageRole.AI,
        content=content,
        parent_message=triggering_message
    )

    thread.active_message = message

    return message
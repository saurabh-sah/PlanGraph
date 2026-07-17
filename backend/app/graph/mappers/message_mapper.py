from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

from app.models.message import Message
from app.models.enums import MessageRole


def to_langchain_message(
    msg: Message,
):

    if msg.role == MessageRole.HUMAN:

        return HumanMessage(
            content=msg.content
        )

    if msg.role == MessageRole.AI:

        return AIMessage(
            content=msg.content
        )

    return SystemMessage(
        content=msg.content
    )

def to_chat_history(
    messages,
):
    return [
        to_langchain_message(m)
        for m in messages
    ]
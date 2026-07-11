from .chat import ChatRequest, ChatResponse
from .health import HealthResponse
from .thread import ThreadCreateRequest, ThreadQuery, ThreadResponse, ThreadUpdateRequest, DeleteThreadResponse
from .message import MessageCreateRequest, MessageResponse

# Add this line to expose the classes
__all__ = [
    "ChatRequest",
    "ChatResponse",
    "HealthResponse",
    "ThreadCreateRequest",
    "ThreadQuery",
    "ThreadResponse",
    "ThreadUpdateRequest",
    "DeleteThreadResponse",
    "MessageCreateRequest",
    "MessageResponse"
]
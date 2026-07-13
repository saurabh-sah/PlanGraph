from enum import Enum


class MessageRole(str, Enum):
    HUMAN = "human"
    AI = "ai"
    SYSTEM = "system"

class AgentRunStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    INTERRUPTED = "interrupted"
    CANCELLED = "cancelled"
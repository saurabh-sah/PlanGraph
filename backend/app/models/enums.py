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

class NodeRunStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"

class NodeType(str, Enum):
    PLANNER = "planner"
    AGENT = "agent"
    TOOL = "tool"
    MCP = "mcp"
    ROUTER = "router"
    MEMORY = "memory"
    RAG = "rag"
    SYNTHESIS = "synthesis"
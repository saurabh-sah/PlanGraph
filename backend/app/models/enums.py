from enum import Enum


class MessageRole(str, Enum):
    HUMAN = "human"
    AI = "ai"
    SYSTEM = "system"

class NodeType(str, Enum):
    PLANNER = "planner"
    AGENT = "agent"
    TOOL = "tool"
    MCP = "mcp"
    ROUTER = "router"
    MEMORY = "memory"
    RAG = "rag"
    SYNTHESIS = "synthesis"

class ExecutionStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
    INTERRUPTED = "interrupted"
    CANCELLED = "cancelled"

class TaskStatus(str, Enum):
    PENDING = "pending"
    READY = "ready"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"
    CANCELLED = "cancelled"

class TaskPriority(
    str,
    Enum
):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class AgentType(
    str,
    Enum
):
    GENERAL = "general"
    RESEARCH = "research"
    CODING = "coding"
    MEMORY = "memory"
    RAG = "rag"
    SYNTHESIS = "synthesis"
    JUDGE = "judge"
    ROUTER = "router"

class MemoryType(
    str,
    Enum
):
    PREFERENCE = "preference"
    FACT = "fact"
    PROJECT = "project"
    RULE = "rule"

class DocumentStatus(
    str,
    Enum
):
    UPLOADING = "uploading"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"
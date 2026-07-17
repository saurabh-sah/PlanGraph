from pydantic import BaseModel, Field
from app.models.enums import (
    AgentType,
    TaskPriority
)

class Dependency(
    BaseModel
):
    task_id: int


class TaskSpec(BaseModel):

    id: int

    title: str

    objective: str

    agent_type: AgentType

    depends_on: list[int] = Field(
        default_factory=list
    )

    priority: TaskPriority = (
        TaskPriority.MEDIUM
    )

    is_terminal: bool = False


class PlannerOutput(BaseModel):

    tasks: list[TaskSpec]

    reasoning: str | None = None
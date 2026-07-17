from pydantic import BaseModel, Field


class Dependency(
    BaseModel
):
    task_id: int


class TaskSpec(BaseModel):

    id: int

    title: str

    objective: str

    agent_type: str

    depends_on: list[int] = Field(
        default_factory=list
    )

    priority: str = "medium"

    is_terminal: bool = False


class PlannerOutput(BaseModel):

    tasks: list[TaskSpec]

    planner_reasoning: str | None = None
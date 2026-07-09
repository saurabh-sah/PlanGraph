from pydantic import BaseModel
from typing import Field

class ThreadCreateRequest(BaseModel):
    title: str
    user_id: int


class ThreadResponse(BaseModel):
    id: int
    title: str
    user_id: int


class ThreadQuery(BaseModel):
    limit: int = Field(default=10, ge=1, lt=100)
    offset: int = Field(default=0, ge=0)

class ThreadUpdateRequest(BaseModel):
    title: str
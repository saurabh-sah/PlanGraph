from pydantic import BaseModel, ConfigDict
from datetime import datetime
from models.enums import MessageRole

class MessageCreateRequest(BaseModel):
    thread_id: int
    content: str

class MessageResponse(BaseModel):

    id: int

    thread_id: int

    parent_message_id: int | None

    role: MessageRole

    content: str

    meta_data: dict | None

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
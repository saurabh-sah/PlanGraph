from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    thread_id: int | None = None


class ChatResponse(BaseModel):
    answer: str
    model: str
    success: bool

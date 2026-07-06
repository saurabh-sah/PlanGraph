from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

class HealthResponse(BaseModel):
    status: Literal["healthy", "unhealthy"]
    database: Literal["connected", "disconnected"]
    version: str

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str
    model: str
    success: bool


@app.get("/health", response_model=HealthResponse)
def get_health():
    return HealthResponse(status="healthy", database="connected", version="1.0.0")

@app.post("/chat", response_model=ChatResponse)
def chat_response(request: ChatRequest):
    return ChatResponse(answer=f"You said: {request.message}", model="fake-llm-v1", success=True)
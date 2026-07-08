from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Literal

import app.models

from app.models.base import Base
from app.db.engine import engine

from sqlalchemy.orm import Session
from app.db.sessions import get_db
from app.services.ThreadService import create_thread, ThreadCreateDTO

Base.metadata.create_all(engine)

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

fake_threads = {
    1: "LangGraph discussion",
    2: "FastAPI notes",
    3: "RAG ideas"
}

@app.get("/health", response_model=HealthResponse)
def get_health():
    return HealthResponse(status="healthy", database="connected", version="1.0.0")

@app.post("/chat", response_model=ChatResponse)
def chat_response(request: ChatRequest):
    return ChatResponse(answer=f"You said: {request.message}", model="fake-llm-v1", success=True)

@app.get("/threads", response_model=list[ThreadResponse], )
def get_threads(thread_info: ThreadQuery = Depends()):
    response: list[ThreadResponse] = []
    remaining = thread_info.limit
    skip = thread_info.offset
    for thread_id, title in fake_threads.items():

        if skip > 0:
            skip -= 1
            continue

        if remaining == 0:
            break

        response.append(
            ThreadResponse(
                thread_id=thread_id,
                title=title
            )
        )

        remaining -= 1
    if not response:
        raise HTTPException(status_code=404, detail="Threads Not Found")
    return response

@app.post("/threads", response_model=ThreadResponse)
def create_thread_route(thread_info: ThreadCreateRequest):
    db: Session = Depends(get_db)
    thread = create_thread(
        db=db,
        thread_info=ThreadCreateDTO(**thread_info.__dict__)
    )
    return ThreadResponse(id=thread.id, title=thread.title, user_id=thread.user_id)



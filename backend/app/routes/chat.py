from app.schemas.chat import ChatRequest, ChatResponse
from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/chat", response_model=ChatResponse)
def chat_response(request: ChatRequest):
    return ChatResponse(
        answer=f"You said: {request.message}",
        model="fake-llm-v1",
        success=True,
    )

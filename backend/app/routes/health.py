from app.schemas.health import HealthResponse
from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("/", response_model=HealthResponse)
def get_health():
    return HealthResponse(
        status="healthy",
        database="connected",
        version="1.0.0",
    )

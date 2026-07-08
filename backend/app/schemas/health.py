from pydantic import BaseModel
from typing import Literal

class HealthResponse(BaseModel):
    status: Literal["healthy", "unhealthy"]
    database: Literal["connected", "disconnected"]
    version: str

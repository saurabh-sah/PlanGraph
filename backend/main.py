from app.schemas import *

from fastapi import FastAPI

from app import models
from app.db.engine import engine
from app.models.base import Base

from app.routes import *

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(thread_router)
app.include_router(chat_router)
app.include_router(health_router)
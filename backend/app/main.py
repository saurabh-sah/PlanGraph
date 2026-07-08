from .schemas import *

from fastapi import FastAPI

from . import models
from .db.engine import engine
from .models.base import Base

from .routes import *

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(thread_router)
app.include_router(chat_router)
app.include_router(health_router)
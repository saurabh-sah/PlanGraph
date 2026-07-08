from .thread import router as thread_router
from .chat import router as chat_router
from .health import router as health_router

__all__ =[
    thread_router,
    chat_router,
    health_router
]
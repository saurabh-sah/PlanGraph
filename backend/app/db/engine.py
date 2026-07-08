from sqlalchemy import create_engine
from app.core.config import settings

engine = create_engine(
    str(settings.database_url),
    echo=True,
    pool_pre_ping=True
)
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User


def get_current_user(
    db: Session = Depends(get_db)
) -> User:

    user = db.get(
        User,
        1
    )

    if user is None:
        raise HTTPException(
            status_code=401
        )

    return user
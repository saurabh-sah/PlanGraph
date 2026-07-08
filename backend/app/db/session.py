from sqlalchemy.orm import sessionmaker
from app.db.engine import engine

# session making factory from the same singleton engine
sessionLocal = sessionmaker(
    bind=engine, 
    autoflush=False, 
    expire_on_commit=False
)

def get_db():
    db = sessionLocal() # made a session

    try:
        yield db

    finally:
        db.close()


# yield pauses the func call unlike return which ends the func call, so we get to close the session (here named db) so to not leak connection data, under try block so that session closes even if session throws an error midway

# db.add_thread(..) <- python done
# db.flush(..) <- sql done
# db.commit(..) <- now db performs actions

# we don't want auto flushing, suppose thread.title was None, it would have been flagged but flushed too early, we want explicit control
# expire_on_commit if true, An expired ORM object discards its loaded column values after commit. so every time we run thread.title it queries db again to get the val instead of using the orm obj bcz orm obj got destroyed

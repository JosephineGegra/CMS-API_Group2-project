from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:012345@localhost/SL concert DB"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine

)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # clean up after request

Base = declarative_base()

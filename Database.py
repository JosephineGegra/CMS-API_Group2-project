from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:012345@localhost/SL_Concert_DB"

engine = create_engine(DATABASE_URL, echo=True)

Sessionlocal = sessionmaker(
    autocommit= False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

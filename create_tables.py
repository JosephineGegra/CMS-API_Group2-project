from Database import engine
from Models import Base


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

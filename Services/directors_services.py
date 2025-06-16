from sqlalchemy.orm import Session
from models import Director
import Schema

def create_director(db: Session, director_data: Schema.DirectorCreate):
    director = Director(**director_data.dict())
    db.add(director)
    db.commit()
    db.refresh(director)
    return director

def get_all_directors(db: Session):
    return db.query(Director).all()

def get_director_by_id(db: Session, director_id: int):
    return db.query(Director).filter(Director.id == director_id).first()

def update_director(db: Session, director_id: int, director_data: Schema.DirectorUpdate):
    director = get_director_by_id(db, director_id)
    if director:
        for field, value in director_data.dict(exclude_unset=True).items():
            setattr(director, field, value)
        db.commit()
        db.refresh(director)
    return director

def delete_director(db: Session, director_id: int):
    director = get_director_by_id(db, director_id)
    if director:
        db.delete(director)
        db.commit()
    return director

from sqlalchemy.orm import Session
from Models import Actor
import Schema

def create_actor(db: Session, actor_data: Schema.ActorCreate) -> Actor:
    actor = Actor(**actor_data.dict())
    db.add(actor)
    db.commit()
    db.refresh(actor)
    return actor

def get_all_actors(db: Session):
    return db.query(Actor).all()

def get_actor_by_id(db: Session, actor_id: int):
    return db.query(Actor).filter(Actor.id == actor_id).first()

def update_actor(db: Session, actor_id: int, actor_data: Schema.ActorUpdate):
    actor = get_actor_by_id(db, actor_id)
    if actor:
        for field, value in actor_data.dict(exclude_unset=True).items():
            setattr(actor, field, value)
        db.commit()
        db.refresh(actor)
    return actor

def delete_actor(db: Session, actor_id: int):
    actor = get_actor_by_id(db, actor_id)
    if actor:
        db.delete(actor)
        db.commit()
    return actor
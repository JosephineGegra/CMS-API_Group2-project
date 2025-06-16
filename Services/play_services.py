from sqlalchemy.orm import Session
from Schema import PlayCreate, PlayUpdate, Plays
from models import Play
from typing import List, Optional


def create_play(db: Session, play_data: PlayCreate) -> Play:
    play = Play(**play_data.dict())
    db.add(play)
    db.commit()
    db.refresh(play)
    return play


def get_all_plays(db: Session, skip: int = 0, limit: int = 10) -> List[Play]:
    return db.query(Plays).offset(skip).limit(limit).all()


def get_play_by_id(db: Session, play_id: int) -> Optional[Play]:
    return db.query(Play).filter(Plays.id == play_id).first()


def update_play(db: Session, play_id: int, play_data: PlayUpdate) -> Optional[Play]:
    play = get_play_by_id(db, play_id)
    if not play:
        return None

    for field, value in play_data.dict(exclude_unset=True).items():
        setattr(play, field, value)

    db.commit()
    db.refresh(play)
    return play


def delete_play(db: Session, play_id: int) -> Optional[Play]:
    play = get_play_by_id(db, play_id)
    if not play:
        return None

    db.delete(play)
    db.commit()
    return play

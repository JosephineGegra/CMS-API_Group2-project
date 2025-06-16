from sqlalchemy.orm import Session
from models import ShowTime
import Schema



def create_showtime(db: Session, showtime_data: Schema.ShowtimeCreate):
    showtime = ShowTime(**showtime_data.model_dump())
    db.add(showtime)
    db.commit()
    db.refresh(showtime)
    return showtime

def get_all_showtimes(db: Session):
    return db.query(ShowTime).all()

def get_showtime_by_id(db: Session, showtime_id: int):
    return db.query(ShowTime).filter(ShowTime.id == showtime_id).first()

def update_showtime(db: Session, showtime_id: int, showtime_data: Schema.ShowtimeUpdate):
    showtime = get_showtime_by_id(db, showtime_id)
    if showtime:
        for field, value in showtime_data.model_dump(exclude_unset=True).items():
            setattr(showtime, field, value)
        db.commit()
        db.refresh(showtime)
    return showtime

def delete_showtime(db: Session, showtime_id: int):
    showtime = get_showtime_by_id(db, showtime_id)
    if showtime:
        db.delete(showtime)
        db.commit()
    return showtime
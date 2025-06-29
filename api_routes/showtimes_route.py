from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
import Schema
import Services.showtimes_services as showtime_service
from Models import ShowTime

showtime_route = APIRouter(prefix="/showtimes", tags=["Showtimes"])

@showtime_route.post("/", response_model=Schema.ShowtimeResponse)
def create_showtime(showtime: Schema.ShowtimeCreate, db: Session = Depends(get_db)):
    return showtime_service.create_showtime(db, showtime)

@showtime_route.get("/", response_model=list[Schema.ShowtimeResponse])
def get_all_showtimes(db: Session = Depends(get_db)):
    return showtime_service.get_all_showtimes(db)

@showtime_route.get("/{id}", response_model=Schema.ShowtimeResponse)
def get_showtime(id: int, db: Session = Depends(get_db)):
    showtime = db.query(ShowTime).filter(ShowTime.id == id).first()
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return showtime

@showtime_route.put("/{showtime_id}", response_model=Schema.ShowtimeResponse)
def update_showtime(showtime_id: int, showtime: Schema.ShowtimeUpdate, db: Session = Depends(get_db)):
    updated = showtime_service.update_showtime(db, showtime_id, showtime)
    if not updated:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return updated

@showtime_route.delete("/{showtime_id}")
def delete_showtime(showtime_id: int, db: Session = Depends(get_db)):
    deleted = showtime_service.delete_showtime(db, showtime_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return {"detail": "Showtime deleted"}



from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
import Schema
import Services.showtimes_services as showtime_service

showtime_route = APIRouter(prefix="/showtimes", tags=["Showtimes"])

@showtime_route.post("/", response_model=Schema.Showtime)
def create_showtime(showtime: Schema.ShowtimeCreate, db: Session = Depends(get_db)):
    return showtime_service.create_showtime(db, showtime)

@showtime_route.get("/", response_model=list[Schema.Showtime])
def get_all_showtimes(db: Session = Depends(get_db)):
    return showtime_service.get_all_showtimes(db)

@showtime_route.get("/{showtime_id}", response_model=Schema.Showtime)
def get_showtime(showtime_id: int, db: Session = Depends(get_db)):
    showtime = showtime_service.get_showtime_by_id(db, showtime_id)
    if not showtime:
        raise HTTPException(status_code=404, detail="Showtime not found")
    return showtime

@showtime_route.put("/{showtime_id}", response_model=Schema.Showtime)
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



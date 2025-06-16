from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
import Schema, Services.directors_services as director_service

director_route = APIRouter(prefix="/directors", tags=["Directors"])

@director_route.post("/", response_model=Schema.Director)
def create_director(director: Schema.DirectorCreate, db: Session = Depends(get_db)):
    return director_service.create_director(db, director)

@director_route.get("/", response_model=list[Schema.Director])
def get_all_directors(db: Session = Depends(get_db)):
    return director_service.get_all_directors(db)

@director_route.get("/{director_id}", response_model=Schema.Director)
def get_director(director_id: int, db: Session = Depends(get_db)):
    director = director_service.get_director_by_id(db, director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director

@director_route.put("/{director_id}", response_model=Schema.Director)
def update_director(director_id: int, director: Schema.DirectorUpdate, db: Session = Depends(get_db)):
    updated = director_service.update_director(db, director_id, director)
    if not updated:
        raise HTTPException(status_code=404, detail="Director not found")
    return updated

@director_route.delete("/{director_id}")
def delete_director(director_id: int, db: Session = Depends(get_db)):
    deleted = director_service.delete_director(db, director_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Director not found")
    return {"detail": "Director deleted"}


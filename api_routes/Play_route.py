# routers/play_router.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from Database import get_db
import Schema, Models
from Oauth2 import get_current_user
from Services.play_services import (
    create_play, get_all_plays, get_play_by_id,
    update_play, delete_play
)
from Schema import PlayCreate, PlayUpdate, PlayResponse

router = APIRouter(prefix="/plays", tags=["Plays"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Schema.Plays)
def create_play(play: Schema.PlayCreate, db: Session = Depends(get_db)):
    director = db.query(Models.Director).filter(Models.Director.id == play.director_id).first()
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    db_play = Models.Play(**play.dict())
    db.add(db_play)
    db.commit()
    db.refresh(db_play)
    return db_play


@router.get("/", response_model=list[Schema.PlayResponse])
def read_all_plays(db: Session = Depends(get_db),
                   current_user: Models.User = Depends(get_current_user)
):
    return get_all_plays(db)

@router.get("/{play_id}", response_model=Schema.PlayResponse)
def get_play_route(play_id: int, db: Session = Depends(get_db)):
    play = get_play_by_id(db, play_id)
    if not play:
        raise HTTPException(status_code=404, detail="Play not found")
    return play

@router.put("/{play_id}", response_model=PlayResponse)
def update_play_route(play_id: int, play: PlayUpdate, db: Session = Depends(get_db)):
    updated = update_play(db, play_id, play)
    if not updated:
        raise HTTPException(status_code=404, detail="Play not found")
    return updated

@router.delete("/{play_id}", response_model=PlayResponse)
def delete_play_route(play_id: int, db: Session = Depends(get_db)):
    deleted = delete_play(db, play_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Play not found")
    return deleted

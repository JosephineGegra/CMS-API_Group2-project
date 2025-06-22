from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
import  Models
from Oauth2 import get_current_user
from Services.actor_services import create_actor
import Schema, Services.actor_services as actors_service

actors_route = APIRouter(prefix="/actors", tags=["Actors"])

@actors_route.post("/", response_model=Schema.ActorResponse)  # Changed from Schema.Actor
def create_actor_endpoint(
    actor: Schema.ActorCreate,
    db: Session = Depends(get_db),
    current_user: Models.User = Depends(get_current_user)
):
    return create_actor(db, actor)

@actors_route.get("/", response_model=list[Schema.ActorResponse])
def get_all_actors(db: Session = Depends(get_db),
                   current_user: Models.User = Depends(get_current_user)
):
    return actors_service.get_all_actors(db)

@actors_route.get("/{actor_id}", response_model=Schema.ActorResponse)
def get_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = actors_service.get_actor_by_id(db, actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@actors_route.put("/{actor_id}", response_model=Schema.ActorResponse)
def update_actor(actor_id: int, actor: Schema.ActorUpdate, db: Session = Depends(get_db)):
    updated = actors_service.update_actor(db, actor_id, actor)
    if not updated:
        raise HTTPException(status_code=404, detail="Actor not found")
    return updated

@actors_route.delete("/{actor_id}")
def delete_actor(actor_id: int, db: Session = Depends(get_db)):
    deleted = actors_service.delete_actor(db, actor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Actor not found")
    return {"detail": "Actor deleted"}

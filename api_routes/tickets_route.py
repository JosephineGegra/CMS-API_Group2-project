from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
import  models
from Oauth2 import get_current_user
import Schema, Services.tickets_services as ticket_service

ticket_route = APIRouter(prefix="/tickets", tags=["Tickets"])

@ticket_route.post("/", response_model=Schema.Ticket)
def create_ticket(ticket: Schema.TicketCreate, db: Session = Depends(get_db)):
    return ticket_service.create_ticket(db, ticket)

@ticket_route.get("/", response_model=list[Schema.Ticket])
def get_all_tickets(db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return ticket_service.get_all_tickets(db)

@ticket_route.get("/{ticket_id}", response_model=Schema.Ticket)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = ticket_service.get_ticket_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=402, detail="Ticket not found")
    return ticket

@ticket_route.put("/{ticket_id}", response_model=Schema.Ticket)
def update_ticket(ticket_id: int, ticket: Schema.TicketUpdate, db: Session = Depends(get_db)):
    updated = ticket_service.update_ticket(db, ticket_id, ticket)
    if not updated:
        raise HTTPException(status_code=402, detail="Ticket not found")
    return updated

@ticket_route.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    deleted = ticket_service.delete_ticket(db, ticket_id)
    if not deleted:
        raise HTTPException(status_code=402, detail="Ticket not found")
    return {"detail": "Ticket deleted"}

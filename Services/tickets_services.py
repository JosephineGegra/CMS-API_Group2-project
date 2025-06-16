from sqlalchemy.orm import Session
from models import Ticket
import Schema


def create_ticket(db: Session, ticket_data: Schema.TicketCreate):
    ticket = Ticket(**ticket_data.model_dump())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket

def get_all_tickets(db: Session):
    return db.query(Ticket).all()

def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def update_ticket(db: Session, ticket_id: int, ticket_data: Schema.TicketUpdate):
    ticket = get_ticket_by_id(db, ticket_id)
    if ticket:
        for field, value in ticket_data.model_dump(exclude_unset=True).items():
            setattr(ticket, field, value)
        db.commit()
        db.refresh(ticket)
    return ticket

def delete_ticket(db: Session, ticket_id: int):
    ticket = get_ticket_by_id(db, ticket_id)
    if ticket:
        db.delete(ticket)
        db.commit()
    return ticket
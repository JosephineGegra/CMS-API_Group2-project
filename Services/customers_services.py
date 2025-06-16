from sqlalchemy.orm import Session
from models import Customer
import Schema

def create_customer(db: Session, customer_data: Schema.CustomerCreate):
    customer = Customer(**customer_data.model_dump())
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

def get_all_customers(db: Session):
    return db.query(Customer).all()

def get_customer_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()

def update_customer(db: Session, customer_id: int, customer_data: Schema.CustomerUpdate):
    customer = get_customer_by_id(db, customer_id)
    if customer:
        for field, value in customer_data.model_dump(exclude_unset=True).items():
            setattr(customer, field, value)
        db.commit()
        db.refresh(customer)
    return customer

def delete_customer(db: Session, customer_id: int):
    customer = get_customer_by_id(db, customer_id)
    if customer:
        db.delete(customer)
        db.commit()
    return customer

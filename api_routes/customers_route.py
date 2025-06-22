from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import get_db
import Schema, Models
from Oauth2 import get_current_user
import Schema, Services.customers_services as customer_service

customer_route = APIRouter(prefix="/customers", tags=["Customers"])

@customer_route.post("/", response_model=Schema.CustomerResponse)
def create_customer(customer: Schema.CustomerCreate, db: Session = Depends(get_db)):
    return customer_service.create_customer(db, customer)

@customer_route.get("/", response_model=list[Schema.CustomerResponse])
def get_all_customers(db: Session = Depends(get_db),
                      current_user: Models.User = Depends(get_current_user)
):
    return customer_service.get_all_customers(db)

@customer_route.get("/{customer_id}", response_model=Schema.CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_service.get_customer_by_id(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@customer_route.put("/{customer_id}", response_model=Schema.CustomerResponse)
def update_customer(customer_id: int, customer: Schema.CustomerUpdate, db: Session = Depends(get_db)):
    updated = customer_service.update_customer(db, customer_id, customer)
    if not updated:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated

@customer_route.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    deleted = customer_service.delete_customer(db, customer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"detail": "Customer deleted"}


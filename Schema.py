from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Play(BaseModel):
    PlayId: int
    Title: str
    Duration: int
    Genre: str
    Synopsis: Optional[str] = None


class Actor(BaseModel):
    ActorId: int
    Name: str
    Gender: str
    DateOfBirth: Optional[int] = None


class Director(BaseModel):
    DirectorId: int
    Name: str
    DateOfBirth: int
    Citizenship: Optional[str] = None


class Customer(BaseModel):
    CustomerId: int
    Name: str
    TelephoneNo: int


class Seat(BaseModel):
    RowNo: int
    SeatNo: int


class ShowTimes(BaseModel):
    DateAndTime: datetime
    Play_PlayId: int


class Ticket(BaseModel):
    Seat_RowNo: int
    Seat_SeatNo: int
    ShowTimes_DateAndTime: datetime
    ShowTimes_Play_PlayId: int
    Customer_CustomerId: int
    TicketNo: str


class Price(BaseModel):
    Seat_RowNo: int
    Seat_SeatNo: int
    ShowTimes_DateAndTime: datetime
    ShowTimes_Play_PlayId: int
    Price: float


class Actor_Play(BaseModel):
    ActorId: int
    PlayId: int


class Director_Play(BaseModel):
    DirectorId: int
    PlayId: int

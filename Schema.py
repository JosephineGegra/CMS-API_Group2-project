from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import date, datetime



class Plays(BaseModel):
    id: int
    title: str
    duration_minutes: int
    genre: str
    description: Optional[str] = None
    director_id: Optional[int] = None



class Actor(BaseModel):
    Id: int
    name: str
    gender: str
    DateOfBirth: Optional[date] = None


class Director(BaseModel):
    id: int
    name: str
    date_of_birth: date
    citizenship: Optional[str] = None


class Customer(BaseModel):
    CustomerId: int
    Name: str
    TelephoneNo: int


class Seat(BaseModel):
    RowNo: int
    SeatNo: int


class Showtime(BaseModel):
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


class actor_Play(BaseModel):
    ActorId: int
    PlayId: int


class director_Play(BaseModel):
    DirectorId: int
    PlayId: int

#play schemas

class PlayBase(BaseModel):
    title: str
    genre: str
    description: Optional[str] = None
    duration_minutes: int
    director_id: int


class PlayCreate(PlayBase):
    pass


class PlayUpdate(PlayBase):
    title: Optional[str] = None
    genre: Optional[str] = None
    description: Optional[str] = None
    duration_minutes: Optional[int] = None
    director_id: Optional[int] = None

class PlayResponse(PlayBase):
    id: int

    class Config:
        from_attributes = True


#Actors Schemas
class ActorBase(BaseModel):
    name: str
    gender: str
    DateOfBirth: Optional[date] = None

    @validator("gender")
    def validate_gender(cls, value):
        gender_map = {
            "Male": "M",
            "Female": "F",
            "M": "M",
            "F": "F"
        }
        if value not in gender_map:
            raise ValueError("Gender must be 'Male', 'Female', 'M', or 'F'")
        return gender_map[value]

class ActorCreate(ActorBase):
    pass

class ActorUpdate(ActorBase):
    name: Optional[str] = None
    gender: Optional[str] = None
    DateOfBirth: Optional[date] = None

class ActorResponse(ActorBase):
    id: int

    class Config:
        from_attributes = True

#customer schemas

class CustomerBase(BaseModel):
    name: str
    telephone_no: Optional[str] = None  # Changed to str because phone numbers may contain +, - etc.

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    telephone_no: Optional[str] = None

class CustomerResponse(CustomerBase):
    id: int

    class Config:
        from_attributes = True


#Tickets schema
class TicketBase(BaseModel):

    seat_number: int
    showtime_id: int
    customer_id: int


class TicketCreate(TicketBase):
    pass

class TicketUpdate(BaseModel):
    seat_number: int
    showtime_id: int
    customer_id: int

class TicketResponse(TicketBase):
    id: int

    class Config:
        from_attributes = True
#Directors schema

class DirectorBase(BaseModel):
    name: str
    date_of_birth: Optional[date] = None
    citizenship: Optional[str] = "Sierra Leonean"  # Set default to "Sierra Leonean"

class DirectorCreate(DirectorBase):
    pass

class DirectorUpdate(DirectorBase):
    name: Optional[str] = None
    date_of_birth: Optional[date] = None
    citizenship: Optional[str] = None

class DirectorResponse(DirectorBase):
    id: int

    class Config:
        from_attributes = True


#Showtimes schema
class ShowtimeBase(BaseModel):
    play_id: int
    show_time: datetime

class ShowtimeCreate(ShowtimeBase):
    pass

class ShowtimeUpdate(ShowtimeBase):
    play_id: Optional[int] = None
    show_time: Optional[datetime] = None

class ShowtimeResponse(ShowtimeBase):
    id: int

    class Config:
        from_attributes = True

class PriceBase(BaseModel):
    seat_row_no: int
    seat_seat_no: int
    showtime_date_time: datetime
    showtime_play_id: int
    price: float

class PriceCreate(PriceBase):
    pass

class PriceUpdate(BaseModel):
    seat_row_no: Optional[int] = None
    seat_seat_no: Optional[int] = None
    showtime_date_time: Optional[datetime] = None
    showtime_play_id: Optional[int] = None
    price: Optional[float] = None

class PriceResponse(PriceBase):
    id: int

    class Config:
        from_attributes = True

#seats schema
class SeatBase(BaseModel):
    row_no: int
    seat_no: int

class SeatCreate(SeatBase):
    pass

class SeatUpdate(BaseModel):
    row_no: Optional[int] = None
    seat_no: Optional[int] = None

class SeatResponse(SeatBase):
    id: int

    class Config:
        from_attributes = True

# Many-to-Many relation schemas
# actor_play
# -------------------------
class ActorPlayBase(BaseModel):
    actor_id: int
    play_id: int

class ActorPlayCreate(ActorPlayBase):
    pass

class ActorPlayResponse(ActorPlayBase):
    id: int

    class Config:
        from_attributes = True


# director_play
# -------------------------
class DirectorPlayBase(BaseModel):
    director_id: int
    play_id: int

class DirectorPlayCreate(DirectorPlayBase):
    pass

class DirectorPlayResponse(DirectorPlayBase):
    id: int

    class Config:
        from_attributes = True



class Login(BaseModel):
    email: EmailStr
    password: str

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

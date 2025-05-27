from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, CHAR, DECIMAL
from sqlalchemy.orm import relationship
from Database import Base


Actor_Play = Table(
    'Actor_Play', Base.metadata,
    Column('ActorId', Integer, ForeignKey('Actor.ActorId'), primary_key=True),
    Column('PlayId', Integer, ForeignKey('Play.PlayId'), primary_key=True)
)

Director_Play = Table(
    'Director_Play', Base.metadata,
    Column('DirectorId', Integer, ForeignKey('Director.DirectorId'), primary_key=True),
    Column('PlayId', Integer, ForeignKey('Play.PlayId'), primary_key=True)
)

class Play(Base):
    __tablename__ = 'Play'
    PlayId = Column(Integer, primary_key=True)
    Title = Column(String(100))
    Duration = Column(Integer)
    Genre = Column(String(20))
    Synopsis = Column(String(2000))

    actors = relationship("Actor", secondary=Actor_Play, back_populates="plays")
    directors = relationship("Director", secondary=Director_Play, back_populates="plays")
    showtimes = relationship("ShowTimes", back_populates="play")

class Actor(Base):
    __tablename__ = 'Actor'
    ActorId = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Gender = Column(CHAR(1))
    DateOfBirth = Column(Integer)

    plays = relationship("Play", secondary=Actor_Play, back_populates="actors")

class Director(Base):
    __tablename__ = 'Director'
    DirectorId = Column(Integer, primary_key=True)
    Name = Column(String(100))
    DateOfBirth = Column(Integer)
    Citizenship = Column(String(100))

    plays = relationship("Play", secondary=Director_Play, back_populates="directors")

class Customer(Base):
    __tablename__ = 'Customer'
    CustomerId = Column(Integer, primary_key=True)
    Name = Column(String(100))
    TelephoneNo = Column(String(100))

    tickets = relationship("Ticket", back_populates="customer")

class Seat(Base):
    __tablename__ = 'Seat'
    RowNo = Column(Integer, primary_key=True)
    SeatNo = Column(Integer, primary_key=True)

class ShowTimes(Base):
    __tablename__ = 'ShowTimes'
    DateAndTime = Column(DateTime, primary_key=True)
    Play_PlayId = Column(Integer, ForeignKey('Play.PlayId'), primary_key=True)

    play = relationship("Play", back_populates="showtimes")
    tickets = relationship("Ticket", back_populates="showtime")

class Ticket(Base):
    __tablename__ = 'Ticket'
    Seat_RowNo = Column(Integer, primary_key=True)
    Seat_SeatNo = Column(Integer, primary_key=True)
    ShowTimes_DateAndTime = Column(DateTime, primary_key=True)
    ShowTimes_Play_PlayId = Column(Integer, primary_key=True)
    Customer_CustomerId = Column(Integer, ForeignKey('Customer.CustomerId'), primary_key=True)
    TicketNo = Column(String(10))

    customer = relationship("Customer", back_populates="tickets")
    showtime = relationship("ShowTimes", back_populates="tickets")

class Price(Base):
    __tablename__ = 'Price'
    Seat_RowNo = Column(Integer, primary_key=True)
    Seat_SeatNo = Column(Integer, primary_key=True)
    ShowTimes_DateAndTime = Column(DateTime, primary_key=True)
    ShowTimes_Play_PlayId = Column(Integer, primary_key=True)
    Price = Column(DECIMAL(10,2))

from sqlalchemy import Column, Integer, String, ForeignKey, Table, CHAR, Date, DateTime
from sqlalchemy.orm import relationship
from Database import Base

# Association Tables
Actor_Play = Table(
    'actor_play', Base.metadata,
    Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True),
    Column('play_id', Integer, ForeignKey('plays.id'), primary_key=True)
)

# Play-Director is now one-to-many (a director has many plays), so no association table needed

# Models

class Play(Base):
    __tablename__ = "plays"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    duration_minutes = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    director_id = Column(Integer, ForeignKey("directors.id"))

    director = relationship("Director", back_populates="plays")
    showtimes = relationship("ShowTime", back_populates="play")
    actors = relationship("Actor", secondary=Actor_Play, back_populates="plays")



class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    gender = Column(CHAR(6))
    DateOfBirth = Column(Date)


    plays = relationship("Play", secondary=Actor_Play, back_populates="actors")


class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    date_of_birth = Column(Date)
    citizenship = Column(String(100), nullable=True)

    plays = relationship("Play", back_populates="director")


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    telephone_no = Column(String(100))

    tickets = relationship("Ticket", back_populates="customer")


class Seat(Base):
    __tablename__ = 'seats'
    row_no = Column(Integer, primary_key=True)
    seat_no = Column(Integer, primary_key=True)

class ShowTime(Base):
    __tablename__ = "showtimes"

    id = Column(Integer, primary_key=True, index=True)
    show_time = Column(DateTime, nullable=False)
    play_id = Column(Integer, ForeignKey("plays.id"), nullable=False)

    play = relationship("Play", back_populates="showtimes")
    tickets = relationship("Ticket", back_populates="showtime")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    seat_number = Column(String, nullable=False)
    showtime_id = Column(Integer, ForeignKey("showtimes.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    showtime = relationship("ShowTime", back_populates="tickets")
    customer = relationship("Customer", back_populates="tickets")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)

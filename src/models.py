from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(120), nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

 
    favorites: Mapped[List["Favorites"]] = relationship("Favorites", back_populates="user", cascade="all, delete-orphan")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname
        }


class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    planet: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship("Favorites", back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "planet": self.planet
        }


class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    character: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)


    favorites: Mapped[List["Favorites"]] = relationship("Favorites", back_populates="character")

    def serialize(self):
        return {
            "id": self.id,
            "character": self.character
        }


class Vehicles(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    vehicle: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)

    
    favorites: Mapped[List["Favorites"]] = relationship("Favorites", back_populates="vehicle")

    def serialize(self):
        return {
            "id": self.id,
            "vehicle": self.vehicle
        }


class Favorites(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    character_id: Mapped[Optional[int]] = mapped_column(ForeignKey("characters.id"))
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planets.id"))
    vehicle_id: Mapped[Optional[int]] = mapped_column(ForeignKey("vehicles.id"))

   
    user: Mapped["User"] = relationship("User", back_populates="favorites")
    character: Mapped[Optional["Characters"]] = relationship("Characters", back_populates="favorites")
    planet: Mapped[Optional["Planets"]] = relationship("Planets", back_populates="favorites")
    vehicle: Mapped[Optional["Vehicles"]] = relationship("Vehicles", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }

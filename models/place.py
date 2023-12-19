#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)

    description = Column(String(1024))

    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)

    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review", cascade="all, delete, delete-orphan", backref="place"
        )
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            back_populates="place_amenities",
            viewonly=False,
        )
    else:

        @property
        def reviews(self):
            dictionary = models.storage.all()
            _list = []
            for key in dictionary:
                key = shlex.split(key.replace(".", " "))
                if key[0] == "Review":
                    _list.append(dictionary[key])
            return [item for item in _list if item.place_id == self.id]

        @property
        def amenities(self):
            return self.amenity_ids

        @amenities.setter
        def amenities(self, amenity=None):
            """Setter method for amenities"""
            if type(amenity) is Amenity and amenity.id not in self.amenity_ids:
                self.amenity_ids.append(amenity.id)

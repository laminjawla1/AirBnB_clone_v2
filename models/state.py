#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
import models
from os import getenv
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="all, delete", backref="state")
    else:

        @property
        def cities(self):
            """Returns all cities of a specific state"""
            _list = []
            for city in models.storage.all().values():
                if city.state_id == self.id:
                    _list.append(city)
            return _list

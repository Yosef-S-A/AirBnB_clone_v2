#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """Returns the list of City instances corresponding to this state"""
        from models import storage
        my_cities = storage.all(City)
        state_city = [cc for cc in my_cities if cc.state_id == self.id]
        return state_city

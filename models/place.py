#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False)
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    reviews = relationship("Review", backref="place",
                           cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity", secondary=place_amenity,
                             back_populates="place_amenities", viewonly=False)

    @property
    def reviews(self):
        """Returns a list of 'Review' instances for this place"""
        from models import storage
        all_reviews = storage.all(Review)
        my_reviews = [rr for rr in all_reviews if rr.place_id == self.id]
        return my_reviews

    @property
    def amenities(self):
        """Return a list of 'Amenity' instances for this place"""
        my_amenities = [amen for amen in amenities where amen.id in
                        self.amenity_ids]

    @amenities.setter
    def amenities(self, value):
        """Add amenity id of amenity available at this place in amenity_ids"""
        if (type(value) is Amenity):
            amenity_ids.append(value.id)

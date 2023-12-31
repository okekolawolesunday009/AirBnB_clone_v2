#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from os import getenv

place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name =  Column(String(128), nullable=False)
    description =  Column(String(1024))
    number_rooms =  Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', cascade='all, delete-orphan', backref='place')

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", secondary="place_amenity",
                viewonly=False, 
                backref="place_amenities",
                primaryjoin="Place.id == place_amenity.c.place_id",
                secondaryjoin="Amenity.id == place_amenity.c.amenity_id")
    
    else:
        @property
        def reviews(self):
            """returns the list of Review instances"""
            var = models.FileStorage.all(Review).values()
            lis = []
            result = []
            for key in var:
                review = key.replace(".", " ")
                review = review.split()
                if review[0] == "review":
                    lis.append(var[key])
            for elem in lis:
                if (elem.place_id == self.id):
                    result.append(elem)
            return result
        @property
        def amenities(self):
            """that returns the list of Amenity"""
            return self.amenity_ids
        
        @amenities.setter
        def amenities(self, obj=None):
            """Appends amenity ids to the attribute"""
            if type(obj) == "Amenity" and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)

#!/usr/bin/python3
"""
State Module for HBNB project

This module defines the Amenity class which inherits from BaseModel and Base.
Amenity objects represent amenities that can be associated with places.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity class for HBNB project.

    Attributes:
        __tablename__ (str): The name of the database table for Amenity objects.
        name (sqlalchemy.Column): The name of the amenity. This is a required field.
        place_amenities (sqlalchemy.orm.relationship): A relationship to the PlaceAmenity
            association object. This is currently commented out.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)  # The name of the amenity
    # place_amenities = relationship('Place')  # Relationship to PlaceAmenity association object

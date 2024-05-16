#!/usr/bin/python3
"""
Review module for the HBNB project

This module defines the Review class, which inherits from BaseModel and Base.
The Review class is used to store review information for a specific place.
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    Review class to store review information

    Attributes:
        __tablename__ (str): The name of the database table for Review objects.
        place_id (Column): The ID of the place being reviewed, represented as a string.
                            This is a foreign key referencing the 'places' table.
        user_id (Column): The ID of the user who wrote the review, represented as a string.
                           This is a foreign key referencing the 'users' table.
        text (Column): The text content of the review, represented as a string.
    """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)

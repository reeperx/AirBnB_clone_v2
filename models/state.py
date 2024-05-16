#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """
    State class
    Inherits from BaseModel and Base classes
    Represents a state in the application
    """
    __tablename__ = 'states'  # Name of the table in the database
    name = Column(String(128), nullable=False)  # Column for storing the state name (required)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')  # Relationship with City class

    # Conditional block for handling file storage
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        from models import storage
        from models.city import City

        @property
        def cities(self):
            """
            Property method that returns the list of City instances
            with state_id equals to the current State.id
            Used for file storage
            """
            c = storage.all(City)  # Get all City instances from file storage
            return [v for v in c.values() if v.state_id == self.id]  # Filter cities by state_id

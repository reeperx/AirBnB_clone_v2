#!/usr/bin/python3
""" City Module for HBNB project """
# Importing necessary modules
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    # Defining the table name
    __tablename__ = 'cities'
    
    # Defining the columns
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    # state_id column is a string of maximum length 60, a foreign key referencing the 'id' column of the 'states' table, and cannot be null
    name = Column(String(128), nullable=False)
    # name column is a string of maximum length 128 and cannot be null
    places = relationship('Place',
                          cascade='all, delete-orphan', backref='cities')
    # places is a relationship with the 'Place' class, with cascade options 'all' and 'delete-orphan', and a backref to access the related City object from a Place instance

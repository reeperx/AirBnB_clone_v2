#!/usr/bin/python3
"""This module defines a class User"""
# Import the BaseModel and Base classes from the models.base_model module
from models.base_model import (BaseModel, Base)
# Import the Column, Integer, and String classes from the sqlalchemy module
from sqlalchemy import (Column, Integer, String)
# Import the relationship function from the sqlalchemy.orm module
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    This class defines a user by various attributes

    Attributes:
        email (str): The email address of the user (required)
        password (str): The password of the user (required)
        first_name (str): The first name of the user (optional)
        last_name (str): The last name of the user (optional)
        places (list): A list of Place objects associated with the user
        reviews (list): A list of Review objects associated with the user
    """
    # Define the table name for the User class in the database
    __tablename__ = 'users'
    # Define the email column as a non-nullable string with a maximum length of 128 characters
    email = Column(String(128), nullable=False)
    # Define the password column as a non-nullable string with a maximum length of 128 characters
    password = Column(String(128), nullable=False)
    # Define the first_name column as a nullable string with a maximum length of 128 characters
    first_name = Column(String(128))
    # Define the last_name column as a nullable string with a maximum length of 128 characters
    last_name = Column(String(128))
    # Define a one-to-many relationship between User and Place objects
    # The 'backref' parameter allows Place objects to access the associated User object
    # The 'cascade' parameter specifies that when a User object is deleted, all associated Place objects should also be deleted
    places = relationship('Place',
                          backref='user', cascade='all, delete-orphan')
    # Define a one-to-many relationship between User and Review objects
    # The 'cascade' parameter specifies that when a User object is deleted, all associated Review objects should also be deleted
    # The 'backref' parameter allows Review objects to access the associated User object
    reviews = relationship('Review',
                           cascade='all, delete-orphan', backref='user')

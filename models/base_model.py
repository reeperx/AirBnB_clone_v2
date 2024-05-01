#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

# Create a declarative base for SQLAlchemy
Base = declarative_base()


class BaseModel():
    """A base class for all hbnb models"""

    # Define columns for the BaseModel class
    id = Column(String(60), unique=True, nullable=False,
                primary_key=True)  # Unique id for each instance
    created_at = Column(DateTime, nullable=False,
                        default=datetime.now())  # Creation time of instance
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.now())  # Last update time of instance

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model
        Args:
            *args: Unused
            **kwargs: Key/value pair of attributes
        """
        if 'updated_at' not in kwargs.keys():  # If instance is being created
            self.id = str(uuid.uuid4())  # Generate unique id
            self.created_at = datetime.now()  # Set creation time
            self.updated_at = datetime.now()  # Set update time
        else:  # If instance is being loaded from storage
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']  # Remove __class__ from kwargs
        self.__dict__.update(kwargs)  # Update instance attributes

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]  # Get class name
        props = self.__dict__.copy()  # Copy instance attributes
        if '_sa_instance_state' in props.keys():  # Remove SQLAlchemy attribute
            del (props['_sa_instance_state'])
        return '[{}] ({}) {}'.format(cls, self.id, props)  # Return string

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage  # Import storage engine
        self.updated_at = datetime.now()  # Update update time
        storage.new(self)  # Add instance to storage
        storage.save()  # Save storage

    def delete(self):
        """deletes current instance from the storage"""
        from models import storage  # Import storage engine
        storage.delete(self)  # Delete instance from storage
    def to_dict(self):
        """Convert instance into dict format"""
        if '_sa_instance_state' in self.__dict__.keys():  # Remove SQLAlchemy attribute
            del (self.__dict__['_sa_instance_state'])
        dictionary = {}
        dictionary.update(self.__dict__)  # Copy instance attributes
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})  # Add class name
        dictionary['created_at'] = self.created_at.isoformat()  # Convert datetime to string
        dictionary['updated_at'] = self.updated_at.isoformat()  # Convert datetime to string
        return dictionary  # Return dictionary representation

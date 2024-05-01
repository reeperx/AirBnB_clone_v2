#!/usr/bin/python3
"""BDStorage Engine"""
# Importing necessary modules
import os
from sqlalchemy import (create_engine, MetaData)  # For creating the engine and metadata
from sqlalchemy.orm import (sessionmaker, scoped_session)  # For creating sessions
from models.base_model import (BaseModel, Base)  # Base classes for models
from models.state import State  # State model
from models.amenity import Amenity  # Amenity model
from models.place import Place  # Place model
from models.user import User  # User model
from models.city import City  # City model
from models.review import Review  # Review model

class DBStorage():
    """
    This class handles the storage of data in a database.
    It creates an engine and a session, and provides methods
    to interact with the database.
    """
    __engine = None  # Engine object for the database
    __session = None  # Session object for the database
    models = {"State": State,
              "Place": Place, "User": User, "City": City,
              "Amenity": Amenity, "Review": Review}  # Dictionary of models

    def __init__(self):
        """
        Initializes the engine object with the database connection details.
        If the environment is set to 'test', it drops all tables in the database.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB'),
                                             ),
                                      pool_pre_ping=True
                                      )
        if (os.getenv('HBNB_ENV') == 'test'):
            metadata = MetaData()
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries all objects of a specific class (or all classes if none is provided)
        from the current database session and returns them as a dictionary.
        """
        objects = {}
        if not cls:
            for k, v in self.models.items():
                table = self.__session.query(v)
                objects.update({(k + row.id): row for row in table})
        else:
            classname = cls.__name__
            table = self.__session.query(cls)
            objects.update({(classname + '.' + row.id): row for row in table})
        return objects

    def new(self, obj):
        """
        Adds a new object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the current database session.
        """
        self.__session.commit()

    def delete(self, obj):
        """
        Deletes an object from the current database session if it is not None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and creates a new session.
        """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

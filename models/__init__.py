#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
# Import the os module to interact with the operating system
import os


# Check the value of the environment variable 'HBNB_TYPE_STORAGE'
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    # If the value is 'db', import the DBStorage class from the db_storage module
    # and alias it as Storage
    from models.engine.db_storage import DBStorage as Storage
else:
    # If the value is not 'db', import the FileStorage class from the file_storage module
    # and alias it as Storage
    from models.engine.file_storage import FileStorage as Storage

# Create an instance of the Storage class (either DBStorage or FileStorage)
storage = Storage()

# Call the reload method on the storage instance to load data from the storage
storage.reload()

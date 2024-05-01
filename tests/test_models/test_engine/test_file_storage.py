#!/usr/bin/python3
""" Module for testing file storage"""
# Importing necessary modules and classes
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        # Clearing the __objects dictionary before each test
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        # Removing the 'file.json' file after each test
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        # Checking if the __objects dictionary is empty at the start
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        # Creating a new BaseModel object
        new = BaseModel()
        # Checking if the new object is added to the __objects dictionary
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        # Creating a new BaseModel object
        new = BaseModel()
        # Checking if the all() method returns a dictionary
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        # Creating a new BaseModel object
        new = BaseModel()
        # Checking if the 'file.json' file is not created when a new object is instantiated
        self.assertFalse(os.path.exists('file.json'))
        self.assertFalse(os.path.exists('file.json'))
    def test_empty(self):
        """ Data is saved to file """
        # Creating a new BaseModel object
        new = BaseModel()
        # Converting the new object to a dictionary
        thing = new.to_dict()
        # Saving the new object to the file
        new.save()
        # Creating a new object from the dictionary
        new2 = BaseModel(**thing)
        # Checking if the 'file.json' file is not empty
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        # Creating a new BaseModel object
        new = BaseModel()
        # Calling the save() method of the FileStorage class
        storage.save()
        # Checking if the 'file.json' file exists
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        # Creating a new BaseModel object
        new = BaseModel()
        # Saving the new object to the file
        storage.save()
        # Reloading the data from the file
        storage.reload()
        # Checking if the loaded object has the same ID as the original object
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        # Creating an empty 'file.json' file
        with open('file.json', 'w') as f:
            pass
        # Checking if a ValueError is raised when trying to load from an empty file
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        # Checking if None is returned when trying to load from a non-existent file
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        # Creating a new BaseModel object
        new = BaseModel()
        # Calling

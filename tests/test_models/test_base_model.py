#!/usr/bin/python3
"""
This module contains a test suite for the BaseModel class.
"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """
    This class defines a test suite for the BaseModel class.
    It inherits from the unittest.TestCase class.
    """

    def __init__(self, *args, **kwargs):
        """
        This is the constructor for the test_basemodel class.
        It initializes the name and value attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        This method is called before each test method is executed.
        It does not perform any setup operations in this case.
        """
        pass

    def tearDown(self):
        """
        This method is called after each test method is executed.
        It removes the 'file.json' file if it exists.
        """
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """
        This test method checks if an instance of BaseModel is created correctly.
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        This test method checks if a new instance of BaseModel can be created
        from a dictionary representation of another instance.
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        This test method checks if a TypeError is raised when attempting to create
        an instance of BaseModel with a non-string key in the dictionary.
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """
        This test method checks if the save method of BaseModel correctly
        saves the instance to a JSON file.
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        This test method checks if the string representation of an instance
        of BaseModel is correctly formatted.
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """
        This test method checks if the to_dict method of BaseModel returns
        the correct dictionary representation of an instance.
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        This test method checks if a TypeError is raised when attempting to create
        an instance of BaseModel with a None key in the dictionary.
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """
        This test method checks if a KeyError is raised when attempting to create
        an instance of BaseModel with an invalid key in the dictionary.
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """
        This test method checks if the id attribute of an instance of BaseModel
        is a string.
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
         """
        This test method checks if the created_at attribute of an instance of
        """
        

#!/usr/bin/python3
"""
This module contains a test case for the Amenity class
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    This class inherits from test_basemodel and is used to test the Amenity class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the test_Amenity class
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"  # Set the name attribute to "Amenity"
        self.value = Amenity  # Set the value attribute to the Amenity class
    def test_name2(self):
        """
        Tests if the name attribute of an instance of the Amenity class is a string
        """
        new = self.value()  # Create a new instance of the Amenity class
        self.assertEqual(type(new.name), str)  # Assert that the type of the name attribute is a string

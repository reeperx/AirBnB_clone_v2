#!/usr/bin/python3
"""
This module defines a test case for the City class.
It inherits from the test_basemodel class in the test_models.test_base_model module.
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """
    Test case class for the City class.
    Inherits from the test_basemodel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method for the test_City class.
        Calls the superclass constructor and initializes the name and value attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Test method to check the type of the state_id attribute of the City class.
        Creates a new instance of the City class and asserts that the type of the state_id attribute is a string.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Test method to check the type of the name attribute of the City class.
        Creates a new instance of the City class and asserts that the type of the name attribute is a string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

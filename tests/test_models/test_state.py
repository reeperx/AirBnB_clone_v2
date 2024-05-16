#!/usr/bin/python3
"""
This module contains a test case for the State class, which inherits from the test_basemodel class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    This class defines test cases for the State class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the test_state class.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"  # Set the name attribute to "State"
        self.value = State  # Set the value attribute to the State class
    def test_name3(self):
        """
        Tests if the name attribute of a new State instance is a string.
        """
        new = self.value()  # Create a new instance of the State class
        self.assertEqual(type(new.name), str)  # Assert that the type of the name attribute is a string

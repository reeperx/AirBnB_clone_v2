#!/usr/bin/python3
"""
This module defines the test cases for the Review class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """
    Test cases for the Review class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the test_review class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"  # Set the name attribute to "Review"
        self.value = Review  # Set the value attribute to the Review class
    def test_place_id(self):
        """
        Tests the place_id attribute of the Review class.
        """
        new = self.value()  # Create a new instance of the Review class
        self.assertEqual(type(new.place_id), str)  # Assert that the type of place_id is a string
    def test_user_id(self):
        """
        Tests the user_id attribute of the Review class.
        """
        new = self.value()  # Create a new instance of the Review class
        self.assertEqual(type(new.user_id), str)  # Assert that the type of user_id is a string
    def test_text(self):
        """
        Tests the text attribute of the Review class.
        """
        new = self.value()  # Create a new instance of the Review class
        self.assertEqual(type(new.text), str)  # Assert that the type of text is a string

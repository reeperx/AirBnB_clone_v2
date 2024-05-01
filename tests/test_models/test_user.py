#!/usr/bin/python3
"""
This module defines a test case for the User class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """
    This class defines test cases for the User class.
    It inherits from the test_basemodel class.
    """

    def __init__(self, *args, **kwargs):
        """
        This is the constructor for the test_User class.
        It initializes the name and value attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        This method tests if the first_name attribute of the User class
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        This method tests if the last_name attribute of the User class
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        This method tests if the email attribute of the User class
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        This method tests if the password attribute of the User class
        is of type string.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)

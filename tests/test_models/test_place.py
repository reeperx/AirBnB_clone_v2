#!/usr/bin/python3
"""
This module contains the test cases for the Place class.
"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """
    This class defines test cases for the Place class.
    It inherits from the test_basemodel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of the test_Place class.
        Sets the name and value attributes.
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Tests if the city_id attribute of the Place instance is a string.
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Tests if the user_id attribute of the Place instance is a string.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Tests if the name attribute of the Place instance is a string.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Tests if the description attribute of the Place instance is a string.
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Tests if the number_rooms attribute of the Place instance is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Tests if the number_bathrooms attribute of the Place instance is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Tests if the max_guest attribute of the Place instance is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Tests if the price_by_night attribute of the Place instance is an integer.
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Tests if the latitude attribute of the Place instance is a float.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Tests if the longitude attribute of the Place instance is a float.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """
        Tests if the amenity_ids attribute of the Place instance is a list.
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

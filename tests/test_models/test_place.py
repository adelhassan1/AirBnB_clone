#!/usr/bin/python3
""" Test place"""
import unittest
from models.place import Place

class My_place_test(unittest.TestCase):
    """
    class to define the test caseses for the place
    """
    def test_city_id(self):
        """
        To check if the city_id is a string or not
        """
        self.assertTrue(isinstance(city_id, str), "city_id must be a str")

    def test_user_id(self):
        """
        To check if the user_id is a str or not
        """
        self.assertTrue(isinstance(user_id, str), "user_id must be a str")

    def test_name(self):
        """
        To check is the name is a str or not
        """
        self.assertTrue(isinstance(name, str), "name must be a str")

    def test_description(self):
        """
        To check if the description is a str or not
        """
        self.assertTrue(isinstance(description, str), "description must be a str")

    def number_rooms(self):
        """
        To check is the number_rooms is an int or not
        """
        self.assertTrue(isinstance(number_rooms, int), "number_rooms is an int")

    def number_bath(self):
        """
        To check that number of bathroom is an int
        """
        self.assertTrue(isinstance(number_bathrooms, int), "number_bathrooms must be an int")

    def test_max(self):
        """
        To check if the number of guests is an int or not
        """
        self.assertTrue(isinstance(max_guest, int), "max_guest must be an int")

    def test_price_by_night(self):
        """
        To check if the price_by_night is an int
        """
        self.assertTrue(isinstance(price_by_night, int), "price_by_night must be an int")

    def test_latitude(self):
        """
        To check that latitude is a float
        """
        self.assertTrue(isinstance(latitude, float), "latitude must be a float")

    def test_longitude(self):
        """
        To check if the longitude is a float
        """
        self.assertTrue(isinstance(longitude, float), "longitude must be a float"
    
    def test_amenity_ids(self):
        """
        to check if the amenity_ids is a list
        """
        self.assertTrue(isinstance(amenity_ids, list), "amenity_ids must be list")

if __name__ == "__main__":
    unittest.main()


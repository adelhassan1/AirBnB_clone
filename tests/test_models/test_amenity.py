#!/usr/bin/python3
"""The amenity test"""
import unittest
from models.amenity import Amenity

class test_amenty(unittest.TestCase):
    """
    the amenity test case
    """
    def test_name(self):
        """
        check if the name is a str or not
        """
        self.assertTrue(isinstance(name, str), "name must be a str")

if __name__ == "__main__":
    unittest.main()

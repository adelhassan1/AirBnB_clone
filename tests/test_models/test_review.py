#!/usr/bin/python3
"""Test the review module"""

import unittest
from models.review import Review

class Test_review(unittest.TestCase):
    """
    Class to test the review
    """
    def test_place_id(self):
        """
        To check if the place_id is a str or not
        """
        self.assertTrue(isinstance(place_id, str), "Please Enter the correct place_id")

    def test_user_id(self):
        """
        To check if the user_id is a str or not
        """
        self.assertTrue(isinstance(user_id, str), "Please enter the correct user_id")

    def test_text(self):
        """
        To check if the text is a str or not
        """
        self.assertTrue(isinstance(text, str), "Text must be a str")

if __name__ == "__main__":
    unittest.main()


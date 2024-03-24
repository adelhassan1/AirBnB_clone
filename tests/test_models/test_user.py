#!/usr/bin/python3
import unittest
from models.user import User

class My_Test_Cases(unittest.TestCase):
    """
    class: to make the first test case for the class 'User'
    """
    def test_email(self):
        """
        Test if the email is a str or not
        """
        self.assertTrue(isinstance(email, str), "The email must be a str")
    def test_pass(self):
        """
        Test if the password is a str or not
        """
        self.assertTrue(isinstance(password, str), "Password must be a str")
    def test_first_name(self):
        """
        Test if the first_name is a str
        """
        self.assertTrue(isinstance(first_name, str), "First_name must be a str")
    def test_last_name(self):
        """
        Test if the last_name is a str
        """
        self.assertTrue(isinstance(last_name, str), "Last_name must be a str")

if __name__ == "__main__":
    unittest.TestCase


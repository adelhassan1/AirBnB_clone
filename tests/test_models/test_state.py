#!/usr/bin/python3
"""the state test"""
import unittest
from models.state import State

class Test_Case(unittest.TestCase):
    """
    test the state class
    """
    def test_state(self):
        """
        Test if the state is a str or not
        """
        self.assertTrue(isinstance(state, str), "State must be a str")

if __name__ == "__main__":
    unittest.main()


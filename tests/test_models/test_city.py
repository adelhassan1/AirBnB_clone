"""The city test Module"""
import unittest
from models.city import City


class Test_city(unittest.TestCase):
    def test_state_id(self):
        """
        check if the state_id is a str or not
        """
        self.assertTrue(isinstance(state_id, str), "State_id must be a str")
    def test_name(self):
        """
        check if the name is a str or not
        """
        self.assertTrue(isinstance(name, str), "name must be a str")
if __name__ = __main__:
    unittest.main()


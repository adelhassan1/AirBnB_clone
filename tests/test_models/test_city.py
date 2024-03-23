"""The city test Module"""
import unittest
import module:
    >>>city = __import__('city').city

class Test city(unittest.TestCase):
    def test_basic(self):
        loc = type(city('Egypt'))
        if type(city) is not str:
            raise TypeError("state must be a string")
        else:
            self.assertEqual(city, 'Egypt')
        num = type(state_id('246c227a-d5c1-403d-9bc7-6a47bb9f0f68'))
        if type(num) is not int:
            rase TypeError("state_id must be an int")
        else:
            self.assertEqual(num, '246c227a-d5c1-403d-9bc7-6a47bb9f0f68')
if __name__ = __main__:
    unittest.main()

"""The state  test Module"""
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

if __name__ = __main__:
    unittest.main()

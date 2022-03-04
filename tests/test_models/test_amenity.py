#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Class to test Amenity"""

    def test_types(self):
        """test attribute types and class type"""
        model1 = Amenity()
        self.assertEqual(type(model1), Amenity)
        self.assertEqual(type(model1.id), str)
        self.assertEqual(type(model1.created_at), datetime)
        self.assertEqual(type(model1.updated_at), datetime)


if __name__ == '__main__':
    unittest.main()

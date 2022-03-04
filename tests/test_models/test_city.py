#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Class to test City"""

    def test_types(self):
        """test attribute types and class type"""
        model1 = City()
        self.assertEqual(type(model1), City)
        self.assertEqual(type(model1.id), str)
        self.assertEqual(type(model1.created_at), datetime)
        self.assertEqual(type(model1.updated_at), datetime)
        self.assertEqual(type(model1.state_id), str)
        self.assertEqual(type(model1.name), str)


if __name__ == '__main__':
    unittest.main()

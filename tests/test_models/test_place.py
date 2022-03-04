#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Class to test Place"""

    def test_types(self):
        """test attribute types and class type"""
        model1 = Place()
        self.assertEqual(type(model1), Place)
        self.assertEqual(type(model1.id), str)
        self.assertEqual(type(model1.created_at), datetime)
        self.assertEqual(type(model1.updated_at), datetime)


if __name__ == '__main__':
    unittest.main()

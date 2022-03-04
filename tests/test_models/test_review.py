#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Class to test Review"""

    def test_types(self):
        """test attribute types and class type"""
        model1 = Review()
        self.assertEqual(type(model1), Review)
        self.assertEqual(type(model1.id), str)
        self.assertEqual(type(model1.created_at), datetime)
        self.assertEqual(type(model1.updated_at), datetime)


if __name__ == '__main__':
    unittest.main()

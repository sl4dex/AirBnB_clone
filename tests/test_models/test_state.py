#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Class to test State"""

    def test_types(self):
        """test attribute types and class type"""
        model1 = State()
        self.assertEqual(type(model1), State)
        self.assertEqual(type(model1.id), str)
        self.assertEqual(type(model1.created_at), datetime)
        self.assertEqual(type(model1.updated_at), datetime)


if __name__ == '__main__':
    unittest.main()

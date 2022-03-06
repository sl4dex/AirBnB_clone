#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User
from datetime import datetime
from models.engine.file_storage import FileStorage

class TestUser(unittest.TestCase):
    """Class to test User"""
    storage = FileStorage()
    def test_types(self):
        """test attribute types and class type"""
        model1 = User()
        self.assertEqual(type(model1), User)
        self.assertEqual(type(model1.id), str)
        self.assertEqual(type(model1.created_at), datetime)
        self.assertEqual(type(model1.updated_at), datetime)
        self.assertEqual(type(model1.email), str)
        self.assertEqual(type(model1.password), str)
        self.assertEqual(type(model1.first_name), str)
        self.assertEqual(type(model1.last_name), str)


if __name__ == '__main__':
    unittest.main()

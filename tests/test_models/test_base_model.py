#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class to test BaseModel"""
    def test_str(self):
        """test __str__ method"""
        model1 = BaseModel()
        self.assertEqual(str(model1), f'[BaseModel] ({model1.id}) {model1.__dict__}')

    def test_to_dict(self):
        """test to_dict() function"""
        model1 = BaseModel()
        dct = model1.to_dict()
        self.assertEqual(dct['__class__'], 'BaseModel')
        self.assertEqual(dct['created_at'], model1.created_at.isoformat())
        self.assertEqual(dct['updated_at'], model1.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import json
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class to test BaseModel"""
    def test_str(self):
        """test __str__ method"""
        model1 = BaseModel()
        self.assertEqual(str(model1),
                         f'[BaseModel] ({model1.id}) {model1.__dict__}')
        self.assertEqual(type(str(model1)), str)

    def test_to_dict(self):
        """test to_dict() function"""
        model1 = BaseModel()
        dct = model1.to_dict()
        self.assertEqual(dct['__class__'], 'BaseModel')
        self.assertEqual(dct['created_at'], model1.created_at.isoformat())
        self.assertEqual(dct['updated_at'], model1.updated_at.isoformat())
        storage.reload()
        self.assertEqual(dct['__class__'], 'BaseModel')
        self.assertEqual(dct['created_at'], model1.created_at.isoformat())
        self.assertEqual(dct['updated_at'], model1.updated_at.isoformat())

    def test_types(self):
        """test attribute types and class type"""
        model1 = BaseModel()
        self.assertEqual(type(model1), BaseModel)
        self.assertEqual(type(model1.id), str)
        self.assertEqual(type(model1.created_at), datetime)
        self.assertEqual(type(model1.updated_at), datetime)

    def test_fstorage(self):
        """test file storage methods"""
        model1 = BaseModel()
        self.assertEqual(type(storage.all()), dict)

    def test_kwargs(self):
        """test creating a BaseModel instance form a str dict"""
        model1 = BaseModel()
        model2 = BaseModel(**model1.to_dict())
        self.assertEqual(model1.__dict__, model2.__dict__)
        self.assertFalse(model1 is model2)

    def test_Save(self):
        """testing save method"""
        model1 = BaseModel()
        model1.name = "Betty"
        model1.save()
        with open("file.json", "r") as fd:
            obj = json.load(fd)[f"BaseModel.{model1.id}"]
            self.assertEqual(model1.to_dict(), BaseModel(**obj).to_dict())


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import json
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.user import User

class FileStorage(unittest.TestCase):
    """Class to test File Storage"""
    storage = FileStorage()

    def test_all(self):
        """test save method"""
        self.assertEqual(type(self.storage.all()), dict)
        for value in self.storage.all().values():
            self.assertFalse(type(value) is str)
            self.assertFalse(type(value) is dict)
        for key in self.storage.all().keys():
            self.assertTrue(type(key) is str)

    def test_new(self):
        new_instance = BaseModel()
        self.storage.new(new_instance)
        self.assertTrue(self.storage.all()[f'BaseModel.{new_instance.id}'] is new_instance)

    def test_save(self):
        with open("file.json", "w") as fd:
            fd.write("{}")
        self.storage.save()
        with open("file.json", "r") as fd:
            self.assertTrue(fd.read() != "{}")

    def test_reload(self):
        new = BaseModel()
        aux ={}
        aux.update({f'BaseModel.{new.id}': new.to_dict()})
        with open("file.json", "w") as fd:
            fd.write(json.dumps(aux))
        self.storage.reload()
        self.assertTrue(f'BaseModel.{new.id}' in self.storage.all().keys())
        self.assertEqual(self.storage.all()[f'BaseModel.{new.id}'].__str__(), new.__str__())

    def test_reload2(self):
        new_fake = BaseModel()
        new = BaseModel(**new_fake.to_dict())
        aux ={}
        aux.update({f'BaseModel.{new.id}': new.to_dict()})
        with open("file.json", "w") as fd:
            fd.write(json.dumps(aux))
        self.storage.reload()
        self.assertTrue(f'BaseModel.{new.id}' in self.storage.all().keys())
        self.assertEqual(self.storage.all()[f'BaseModel.{new.id}'].__str__(), new.__str__())

    def test_kwargs(self):
        """test creating a BaseModel instance form a str dict"""
        model1 = BaseModel()
        model2 = BaseModel(**model1.to_dict())
        self.storage.new(model2)
        self.assertFalse(model1 is model2)
        self.assertTrue(model2 in self.storage.all().values())


if __name__ == '__main__':
    unittest.main()

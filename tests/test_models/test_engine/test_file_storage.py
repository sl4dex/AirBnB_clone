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
            self.assertTrue(type(value.to_dict()) is dict)
        for key in self.storage.all().keys():
            self.assertTrue(type(key) is str)

    def test_new(self):
        """testing new method"""
        new_instance = BaseModel()
        self.storage.new(new_instance)
        key = f'BaseModel.{new_instance.id}'
        self.assertTrue(self.storage.all()[key] is new_instance)

    def test_save(self):
        """testing save method"""
        with open("file.json", "w") as fd:
            fd.write("{}")
        self.storage.save()
        with open("file.json", "r") as fd:
            self.assertTrue(fd.read() != "{}")

    def test_reload(self):
        """testing reload method"""
        new = BaseModel()
        aux = {}
        key = f'BaseModel.{new.id}'
        aux.update({f'BaseModel.{new.id}': new.to_dict()})
        with open("file.json", "w") as fd:
            fd.write(json.dumps(aux))
        self.storage.all().clear()
        self.storage.reload()
        self.assertTrue(f'BaseModel.{new.id}' in self.storage.all().keys())
        self.assertEqual(self.storage.all()[key].__str__(), new.__str__())

    def test_reload2(self):
        """testing reload method"""
        new_fake = BaseModel()
        new = BaseModel(**new_fake.to_dict())
        aux = {}
        key = f'BaseModel.{new.id}'
        aux.update({f'BaseModel.{new.id}': new.to_dict()})
        with open("file.json", "w") as fd:
            fd.write(json.dumps(aux))
        self.storage.all().clear()
        self.storage.reload()
        self.assertTrue(f'BaseModel.{new.id}' in self.storage.all().keys())
        self.assertEqual(self.storage.all()[key].__str__(), new.__str__())


if __name__ == '__main__':
    unittest.main()

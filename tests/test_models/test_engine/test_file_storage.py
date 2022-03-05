#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import json
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage

class FileStorage(unittest.TestCase):
    """Class to test File Storage"""
    storage = FileStorage()

    def test_all(self):
        """test save method"""
        self.assertEqual(type(self.storage.all()), dict)

    def test_new(self):
        new_instance = BaseModel()
        self.storage.new(new_instance)
        self.assertTrue(new_instance in self.storage.all().values())

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


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
from io import StringIO
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from datetime import datetime
from models import FileStorage
import sys
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """testing Console"""

    storage = FileStorage()
    model1 = BaseModel()

    def cmd(self, *args):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(args[0])
        return f.getvalue().strip("\n")

    def test_create(self):
        self.assertEqual(self.cmd("create"), "** class name missing **")
        self.assertTrue(f'BaseModel.{self.cmd("create BaseModel")}' in self.storage.all().keys())
        self.assertTrue(f'Amenity.{self.cmd("create Amenity")}' in self.storage.all().keys())
        self.assertTrue(f'City.{self.cmd("create City")}' in self.storage.all().keys())
        self.assertTrue(f'Place.{self.cmd("create Place")}' in self.storage.all().keys())
        self.assertTrue(f'Review.{self.cmd("create Review")}' in self.storage.all().keys())
        self.assertTrue(f'State.{self.cmd("create State")}' in self.storage.all().keys())
        self.assertTrue(f'User.{self.cmd("create User")}' in self.storage.all().keys())


    def test_all(self):
        self.assertEqual(self.cmd("all MyModel"), "** class doesn't exist **")

    def test_show(self):
        self.assertEqual(self.cmd("show"), "** class name missing **")
        self.assertEqual(self.cmd("show MyModel"), "** class doesn't exist **")
        self.assertEqual(self.cmd("show BaseModel"), "** instance id missing **")
        self.assertEqual(self.cmd("show BaseModel 121212"), "** no instance found **")

    def test_destroy(self):
        self.assertEqual(self.cmd("destroy"), "** class name missing **")
        self.assertEqual(self.cmd("destroy MyModel"), "** class doesn't exist **")
        self.assertEqual(self.cmd("destroy BaseModel"), "** instance id missing **")
        self.assertEqual(self.cmd("destroy BaseModel 121212"), "** no instance found **")

    def test_update(self):
        self.assertEqual(self.cmd("update"), "** class name missing **")
        self.assertEqual(self.cmd("update MyModel"), "** class doesn't exist **")
        self.assertEqual(self.cmd("update BaseModel"), "** instance id missing **")
        self.assertEqual(self.cmd("update BaseModel 121212"), "** no instance found **")
        self.assertEqual(self.cmd(f"update BaseModel {self.model1.id}"), "** attribute name missing **")
        self.assertEqual(self.cmd(f"update BaseModel {self.model1.id} name"), "** value missing **")


if __name__ == '__main__':
    unittest.main()

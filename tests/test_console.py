#!/usr/bin/python3
"""
Unittest for Console class
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
        """catchs output of cmd"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(args[0])
        return f.getvalue().strip("\n")

    def test_all(self):
        """Testing all command"""
        self.assertEqual(self.cmd("all MyModel"), "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()

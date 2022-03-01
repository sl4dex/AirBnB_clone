#!/usr/bin/python3
""" FileStorage module """
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns object dictionary"""
        return self.__objects

    def new(self, obj):
        """Adds specified object to the __objects dictionary"""
        self.__objects.update({f'{type(obj).__name__}.{obj.id}': obj})

    def reload(self):
        """Loads JSON from file to the __objects dict (if file exists)"""
        try:
            with open(self.__file_path,'r') as fd:
                database = json.load(fd)
                aux = eval(f'{key_aux[0]}(**{database[key]})')
                self.__objects.update({key : aux})
        except Exception as fail:
            return

    def save(self):
        """Saves __objects to file as JSON"""
        with open(f'{self.__file_path}', mode='w+') as fd:
            fd.write(json.dumps(dict(map(lambda x: (x[0], x[1].to_dict()), self.__objects.items()))))

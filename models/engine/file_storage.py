#!/usr/bin/python3
""" FileStorage module """
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
            self.__objects.update({f'{type(obj).__name__}.{obj.id}': obj})

    def reload(self):
        try:
            with open(self.__file_path,'r') as fd:
                database = json.load(fd)
                # for each "object" in the file
                for key in database.keys():
                    key_aux = key.split(".")
				    # aux holds the created instance Class(**valuesdict)
                    aux = eval(f'{key_aux[0]}(**{database[key]})')
                    self.__objects.update({key : aux})
        except Exception as fail:
            return

    def save(self):
        with open(f'{self.__file_path}', mode='w+') as fd:
            fd.write(json.dumps(dict(map(lambda x: (x[0], x[1].to_dict()), self.__objects.items()))))

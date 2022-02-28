#!/usr/bin/python3
""" FileStorage module """
import json
from datetime import datetime
from models.base_model import BaseModel

class FileStorage():
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
            self.__objects.update({f'{type(obj).__name__}.{obj.id}': obj})

    def reload(self):
        try:
            with open(f'{self.__file_path}','r') as fd:
                database = json.load(fd)

                for key in database.keys():
#                    database[key].pop('__class__')
#                    database[key]['created_at'] = datetime.strptime(database[key]['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
#                    database[key]['pdated_at'] = datetime.strptime(database[key]['pdated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    self.__objects.update({key : BaseModel(database[key])})


        except Exception as fail:
            print(fail)
            return

    def save(self):
        with open(f'{self.__file_path}', mode='w+') as fd:
 #           fd.write(json.dumps(self.__objects))
            to_save = self.__objects.copy()
            for key, value in to_save.items():
                to_save[key] = value.to_dict()
            fd.write(json.dumps(to_save))

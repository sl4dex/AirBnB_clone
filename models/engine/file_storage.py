#!/usr/bin/python3
""" FileStorage module """
import json


class FileStorage():
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
            self.__objects.update({f'{type(obj).__name__}.{obj.id}': obj.to_dict()})

    def reload(self):
        try:
            with open(f'{self.__file_path}','r') as fd:
                self.__objects = json.load(fd)
        except Exception as fail:
            return

    def save(self):
        with open(f'{self.__file_path}', mode='w+') as fd:
            fd.write(json.dumps(self.__objects))

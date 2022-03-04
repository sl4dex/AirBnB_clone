#!/usr/bin/python3
""" BaseModel module """
from abc import ABC, abstractmethod
from uuid import uuid4
from datetime import datetime
import models


class BaseModel(ABC):
    """ BaseModel class """
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                setattr(self, key, kwargs[key])
            t = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = t
            t = datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = t
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates updated_at attribute to current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns self.__dict__ but adding class name as a value and
        converting created_at and updated_at as string
        """
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct

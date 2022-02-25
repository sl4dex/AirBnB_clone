#!/usr/bin/python3
""" BaseModel module """
from abc import ABC, abstractmethod
from uuid import uuid4
from datetime import datetime


class BaseModel(ABC):
    """ BaseModel class """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates updated_at attribute to current datetime """
        self.updated_at = datetime.now()

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


b1 = BaseModel()
print("__str__:")
print(b1)
print("---------")
print("__dict__:")
print(b1.__dict__)
print("---------")
print("to_dict():")
print(b1.to_dict())

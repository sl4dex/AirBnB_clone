#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import json
from queue import Empty
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    @staticmethod
    def cls_validate(line):
        """validates class existance and name"""
        if len(line) == 0:
            print("** class name missing **")
            return 1
        for cls in BaseModel.__subclasses__():
            if line[0] == cls.__name__ or line[0] == "BaseModel":
                return 0
        print("** class doesn't exist **")
        return 1

    def do_create(self, line):
        """creates a new instance of the parameter and saves it """
        line = line.split()
        if self.cls_validate(line) == 1:
            return
        new_instance = eval(f'{line[0]}()')
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on
        the class name and id
        """

        line = line.split()
        if self.cls_validate(line) == 1:
            return

        if len(line) < 2:
            print("** instance id missing **")
            return

        if f'{line[0]}.{line[1]}' in models.storage.all().keys():
            print(models.storage.all()[f'{line[0]}.{line[1]}'])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """ destroys specified object """
        line = line.split()
        if self.cls_validate(line) == 1:
            return

        if len(line) < 2:
            print("** instance id missing **")
            return

        if f'{line[0]}.{line[1]}' in models.storage.all().keys():
            del models.storage.all()[f'{line[0]}.{line[1]}']
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints string representation of all instances
        of the specified class
        """

        database = models.storage.all().values()
        if len(line) != 0:
            aux = []
            instances_list = models.storage.all().values()
            for obj in instances_list:
                if type(obj).__name__ == line:
                    aux.append(obj.__str__())
            if len(aux) == 0:
                print("** class doesn't exist **")
            else:
                print(aux)
                return
        else:
            print(list(map(lambda x: x.__str__(), database)))

    def do_update(self, line):
        """ Updates a single value of the specified instance """

        line = line.split()
        if self.cls_validate(line) == 1:
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        # if <class>.<id> is not in __objects{} keys
        if f'{line[0]}.{line[1]}' not in models.storage.all().keys():
            print("** no instance found **")
            return
        if len(line) < 3:
            print("** attribute name missing **")
            return
        if len(line) < 4:
            print("** value missing **")
            return
        database = models.storage.all()
        obj = database[f'{line[0]}.{line[1]}']
        datatype = type(getattr(obj, line[2])).__name__
        # setattr( object, attrname, type(attrvalue) )
        setattr(obj, line[2], eval(f'{datatype}("{line[3]}")'))
        models.storage.save()

    def do_EOF(self, line):
        "Exit the program"
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """do nothing"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()

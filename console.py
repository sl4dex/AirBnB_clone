#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import json
from queue import Empty
from models.base_model import BaseModel
import models
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, line):
        """creates a new instance of the parameter and saves it """
        if len(line) == 0:
            print("** class name missing **")
            return
        line = line.split()
        if line[0] == "BaseModel" or line[0] in [cls.__name__ for cls in BaseModel.__subclasses__()]:
            new_instance = eval(f'{line[0]}()')
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class anme and id"""

        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return

        if line[0] != "BaseModel" and line[0] not in [cls.__name__ for cls in BaseModel.__subclasses__()]:
            print("** class doesn't exist **")
            return

        if len(line) < 2:
            print("** instance id missing **")
            return

        if f'{line[0]}.{line[1]}' in models.storage.all().keys():
                    print(models.storage.all()[f'{line[0]}.{line[1]}'])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return

        if line[0] != "BaseModel" and line[0] not in [cls.__name__ for cls in BaseModel.__subclasses__()]:
            print("** class doesn't exist **")
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
        database = models.storage.all().values()
        if len(line) != 0:
            aux = []
            line = line
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
            print(list(map(lambda x:x.__str__(), database)))

    def do_EOF(self, line):
        "Exit the program"
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """do nothink"""
        return

if __name__ == '__main__':
    HBNBCommand().cmdloop()

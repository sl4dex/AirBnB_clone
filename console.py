#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import re
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
    """Command line interpreter"""
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

    def precmd(self, line):
        """
        Method executed before line is interpreted by cmd
        but after the prompt is generated
        """
        pattern = r'([a-zA-Z]+)\.([a-z]+)\((.*)\)'
        pattern_dict = r'([^,]*), ?(.*)'
        result = re.match(pattern, line)

        if result:
            clase = result.group(1, 2, 3)[0].strip("\"") + " "
            command = result.group(1, 2, 3)[1].strip("\"") + " "
            parentesis = result.group(1, 2, 3)[2].strip("\"") + " "
            if "{" not in parentesis:
                parentesis = parentesis.replace(",", " ")
            else:
                ide = re.match(pattern_dict, parentesis).group(1)
                ide = ide.strip("\"") + " "
                dictionary = re.match(pattern_dict, parentesis).group(2)
                dictionary = dictionary.replace("\'", "\"")
                parentesis = ide + " " + dictionary
            aux = ""
            aux += command + " "
            aux += clase + " "
            aux += parentesis
            return aux
        else:
            return line

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
            if len(aux) == 0 and len(instances_list) != 0:
                print("** class doesn't exist **")
            else:
                print(aux)
                return
        else:
            print(list(map(lambda x: x.__str__(), database)))

    @staticmethod
    def updte(clsname, ide, attrname, attrvalue):
        """update operation for do_update()"""
        database = models.storage.all()
        obj = database[f'{clsname}.{ide}']
        datatype = type(getattr(obj, attrname)).__name__
        if attrname == "amenity_ids":
            obj.attrname.append(attrvalue)
            models.storage.save()
            return
        setattr(obj, attrname, eval(f'{datatype}("{attrvalue}")'))
        models.storage.save()

    def do_update(self, line):
        """ Updates a single value of the specified instance """
        dct_split = line.split(" ", 2)
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
        # if third argument is a dictionary
        if "{" in line[2]:
            dct_split[2] = dct_split[2].replace("\'", "\"")
            dct = json.loads(dct_split[2])
            print(dct)
            for k, v in dct.items():
                # updte (classname, id, attrname, attrvalue)
                self.updte(line[0], line[1], k, v)
        else:
            if len(line) < 4:
                print("** value missing **")
                return
            self.updte(line[0], line[1], line[2], line[3])

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

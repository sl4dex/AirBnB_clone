#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, line):
        """creates a new instance of the parameter and saves it """
        if len(line) == 0:
            print("** class name missing **")
            return
        line = line.split()
        if line[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class anme and id"""

        line = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return

        if line[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(line) < 2:
            print("** instance id missing **")
            return
        try:
            with open("./file.json", "r") as fd:
                database = json.loads(fd.read())

                if f'{line[0]}.{line[1]}' in database.keys():
                    print(database[f'{line[0]}.{line[1]}'])
                    return
        except Exception:
            pass
        finally:
            print("** no instance found **")


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

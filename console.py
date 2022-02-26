#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_create(self, line):
        """creates a new instance of the parameter and saves it """
        if len(line) == 0:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class name missing **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class anme and id"""
        

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

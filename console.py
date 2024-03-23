#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
"""
Entry to command interpreter
"""


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = "(hbnb)"
    classes = {
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
            }

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        print()
        return True

    def emptyline(self):
        "Overwrite default behavior to repeat last cmd"""
        pass

    def do_create(self, line):
        """Creates BaseModel, saves it and prints the id"""
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            model = eval(line)()
            model.save()
            print(model.id)

    def do_show(self, line):
        """Show the string representation: name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Deletes an instance: name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing ** ")

    def do_all(self, line):
        """Print all objects or all objects of specified class"""
        args = line.split()
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append('{}'.format(objs))
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append('{}'.format(objs))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance: name and id"""
        args = line.split()
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

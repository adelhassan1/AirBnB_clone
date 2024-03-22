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
    prompt = "(hbnb) "
    classes = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

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
                obj_list.append("{}".format(objs))
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append("{}".format(objs))
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def update(class_name, id, attribute_name, attribute_value):
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if not id:
            print("** instance id missing **")
            return
        instance = globals()[class_name].get(id)
        if instance is None:
            print("** no instance found **")
            return
        if not attribute_name:
            print("** attribute name missing **")
            return
        if attribute_value is None:
            print("** value missing **")
            return
        if isinstance (attribute_value, str):
            instance.__dict__[attribute_name] = attribute_value
        elif isinstance (attribute_value, int):
            instance.__dict__[attribute_name] = int(attribute_value)
        elif isinstance (attribute_value, float):
            instance.__dict__[attribute_name] = float(attribute_value)
        instance.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3

"""
create a console aribnb
"""
import cmd
import shlex
from posixpath import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_name = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
              "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, args_object):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if args_object == "" or args_object is None:
            print("** class name missing **")
            return
        elif args_object not in class_name:
            print("** class doesn't exist **")
            return
        try:
            evaluate_class = ("{}()".format(args_object))
            instance = eval(evaluate_class)
            instance.save()
            print(instance.id)
        except Exception as fail:
            print("** class doesn't exist **")

    def do_show(self, args_object):

        lines = args_object.split()

        if len(args_object) == 0:
            print("** class name missing **")
            return
        elif lines[0] not in class_name:
            print("** class doesn't exist **")
            return
        elif lines[0] in class_name and len(lines) < 2:
            print("** instance id missing **")
            return
        string_stored = "{}.{}".format(lines[0], lines[1])
        stored_id = storage.all()
        if string_stored in stored_id.keys():
            print(stored_id[string_stored])
        else:
            print("** no instance found **")

    def do_destroy(self, args_object):
        lines = args_object.split()

        if len(args_object) == 0:
            print("** class name missing **")
            return
        elif lines[0] not in class_name:
            print("** class doesn't exist **")
            return
        elif lines[0] in class_name and len(lines) < 2:
            print("** instance id missing **")
            return

        string_stored = "{}.{}".format(lines[0], lines[1])
        stored_id = storage.all()

        if string_stored in stored_id.keys():
            stored_id.pop(string_stored)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args_object):
        lines = args_object.split()
        if len(args_object) == 0:
            list_args = []
            all_classes = storage.all()
            for key, value in all_classes.items():
                list_args.append(value.__str__())
            print(list_args)
        elif lines[0] not in class_name:
            print("** class doesn't exist **")
            return
        elif lines[0] in class_name:
            list_args = []
            all_classes = storage.all()
            for key, value in all_classes.items():
                if lines[0] == value.to_dict()['__class__']:
                    list_args.append(value.__str__())
            print(list_args)

    def do_update(self, args_object):
        lines = shlex.split(args_object)
        stored_id = storage.all()

        if len(args_object) == 0:
            print("** class name missing **")
        elif lines[0] not in class_name:
            print("** class doesn't exist **")
        elif lines[0] in class_name and len(lines) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(lines[0], lines[1]) not in stored_id.keys():
            print("** no instance found **")
        elif len(lines) == 2:
            print("** attribute name missing **")
        elif len(lines) == 3:
            print("** value missing **")
        else:
            try:
                string_key = "{}.{}".format(lines[0], lines[1])
                setattr(stored_id[string_key], lines[2], eval(lines[3]))
                # if string_key in stored_id.keys():
            except NameError:
                setattr(stored_id[string_key], lines[2], (lines[3]))
        storage.save()

    def do_quit(self, args):
        "Exit of commands interpreter"
        return True

    def do_EOF(self, args):
        """End of file cmd"""
        return True

    def emptyline(self, args):
        "When there is an empty line it jumps"
        pass

    def help_quit(self):
        """help_quit"""
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

    def do_create(self, args):
        """Create a new instance of a specified class"""
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Show the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        objects = storage.all(self.classes[class_name])
        if obj_key in objects:
            print(objects[obj_key])
        else:
            print("** no instance found **")

    # Add similar methods for do_destroy, do_all, and do_update

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handle EOF (Ctrl+D) to exit the program"""
        print("")
        return True
 
   def do_create(self, args):
        """ Create an object of any class"""
        try:
            if not args:
                raise SyntaxError()
            arg_list = args.split(" ")
            kw = {}
            for arg in arg_list[1:]:
                arg_splited = arg.split("=")
                arg_splited[1] = eval(arg_splited[1])
                if type(arg_splited[1]) is str:
                    arg_splited[1] = arg_splited[1].replace("_", " ").replace('"', '\\"')
                kw[arg_splited[0]] = arg_splited[1]
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        new_instance = HBNBCommand.classes[arg_list[0]](**kw)
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

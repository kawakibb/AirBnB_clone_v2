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
    classes = {"BaseModel": BaseModel,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review}

    def do_create(self, arg):
        """Create a new instance of a class with given parameters."""
        if not arg:
            print("** class name missing **")
            return

        class_name, *params = arg.split(" ")

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        params = [p.split('=') for p in params if '=' in p]
        obj_dict = {}
        for p in params:
            key, value = p[0], p[1]
            value = value.replace('"', '').replace('_', ' ')
            if '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    pass
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        pass
                    obj_dict[key] = value

                    new_obj = eval(f"{class_name}(**obj_dict)")
                    new_obj.save()
                    print(new_obj.id)

                    if __name__ == "__main__":
                        HBNBCommand().cmdloop()

#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def do_create(self, arg):
    """Create a new instance of a class."""
    if not arg:
        print("** class name missing **")
        return

    args = arg.split()
    class_name = args[0]
    param_pairs = args[1:]

    if class_name not in self.classes:
        print("** class doesn't exist **")
        return

    # Initialize an empty dictionary to hold parameters
    param_dict = {}

    for param_pair in param_pairs:
        # Split the parameter into key and value
        key, value = param_pair.split('=')

        # Process the value according to its type
        if value.startswith('"') and value.endswith('"'):
            # String value
            value = value[1:-1].replace('_', ' ').replace('\\"', '"')
        elif '.' in value:
            # Float value
            value = float(value)
        else:
            # Integer value
            value = int(value)

        # Add the key-value pair to the dictionary
        param_dict[key] = value

    # Create an instance of the specified class with the given parameters
    new_instance = self.classes[class_name](**param_dict)

    # Save the new instance
    new_instance.save()
    print(new_instance.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Return a dictionary of all objects,
        or objects of a specific class if cls is provided.
        """
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {}
            for key, obj in self.__objects.items():
                if obj.__class__ == cls:
                    filtered_objects[key] = obj
            return filtered_objects

    def new(self, obj):
        """
        Add an object to the storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to JSON and save it to the file.
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = obj_dict['__class__']
                    cls = eval(class_name)
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj

    def delete(self, obj=None):
        """
        Delete an object from __objects if it exists.
        If obj is None, the method does nothing.
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

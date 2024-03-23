#!usr/bin/python3
import json
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review
"""
Storage File
"""


class FileStorage:
    """
    FileStorage
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {
            "BaseModel": BaseModel, "User": User, "Place": Place,
            "Amenity": Amenity, "City": City, "Review": Review,
            "State": State}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the obj with key: id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes to the JSON file"""
        my_dict = {}

        for key, val in self.__objects.items():
            my_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """deserialize the JSON file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass

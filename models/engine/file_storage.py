#!usr/bin/python3
import json
from ..base_model import BaseModel
from models.user import User
"""
Storage File
"""


class FileStorage:
    """
    FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets the obj with key: id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes to the JSON file"""
        with open(FileStorage.__file_path, 'w') as file:
            json.dump({
                key: value.to_dict() if not isinstance(value, User) else User(**value.to_dict())
                for key, value in FileStorage.__objects.items()}, file)

    def reload(self):
        """deserialize the JSON file"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = {
                        key: BaseModel(**value) if not 'User' in key else User(**value)
                        for key, value in json.load(file).items()}
        except FileNotFoundError:
            pass

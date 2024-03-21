import json
import BaseModel
class FileStorage:
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
    def save(self):
        with open(FileStorage.__file_path, 'w') as file:
            json.dump({key: value.to_dict() for key, value in FileStorage.__objects.items()}, file)
    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = {key: BaseModel(**value) for key, value in json.load(file).items()}
        except FileNotFoundError:
            pass


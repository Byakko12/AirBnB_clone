#!/usr/bin/python3

"""

"""

from models.base_model import BaseModel
import json


class FileStorage:

    __file_path = "file.json"
    __objects ={}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj is not None:  # <obj class name>.id
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        dict2 = {}
        for key in self.__objects:
            dict2[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dict2, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value['__class__'])(**value)
                    self.__objects[key] = value
        except:
            pass
        
        
#!/usr/bin/python3
"""
File storage 
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

class_name = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,
              "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict object"""
        return self.__objects

    def new(self, obj):
        """set in __objects obj with id <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict2 = {}
        for key in self.__objects:
            dict2[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dict2, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path)"""
        try:
            with open(self.__file_path, "r") as f:
                js_file = json.load(f)
                for key, value in js_file.items():
                    reloaded = class_name[js_file[key]["__class__"]](**js_file[key])
                    self.__objects[key] = reloaded
        except FileNotFoundError:
            pass

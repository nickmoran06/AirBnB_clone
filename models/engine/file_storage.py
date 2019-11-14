#!/usr/bin/python3
"""
Module of the file_storage class
"""

import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[str(obj.__class__.__name__ + "." + obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        ObjDict = {}
        for key, value in self.__objects.items():
            ObjDict[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF8") as MyFile:
            json.dump(ObjDict, MyFile)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            if __file_path:
                with open(self.__file_path, "r") as JsonFile:
                    MyFile = json.load(JsonFile)
        except:
            pass

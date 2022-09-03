#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
           "Review": Review, "Amenity": Amenity, "City": City, "State": State}

""" definition of class 'FileStorage'"""


class FileStorage:
    """ __file_path(stores path to json file)
        __objects(dictionary to store all objects
        in format <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects
    """ new(stores the obj into '__objects' using <class name>.id as key)
    """
    def new(self, obj):
        """ obj is an object of a class to be
            stored int the '__objects' dictionary
        """
        key = type(obj).__name__
        key += "."
        key += obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = FileStorage.__objects
        dict1 = {}
        for key in new_dict.keys():
            dict1[key] = new_dict[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dict1, f)

    def reload(self):
        """ reloads a json file if it exists otherwise do nothing"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
                for obj in new_dict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    cls_name += "()"
                    instance = eval(cls_name)
                    self.new(instance)
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls):
        """
        count the number of objects in storage
        """
        count = 0
        for key in models.storage.all().keys():
            if cls in key:
                count += 1
        return count

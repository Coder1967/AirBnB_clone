#!/usr/bin/python3
<<<<<<< HEAD
"""
Contains the FileStorage class
"""

import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from hashlib import md5

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
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

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            if key == "password":
                json_objects[key].decode()
            json_objects[key] = self.__objects[key].to_dict(save_fs=1)
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

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

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
=======
from models.base_model import BaseModel
import json
""" definition of class 'FileStorage'"""


class FileStorage:
    """ __file_path(stores path to json file)
        __objects(dictionary to store all objects
        in format <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    """ all(returns the dictionary '__objects')"""
    def all(self):
        """ returning the '__objects' dict"""
        return FileStorage.__objects

    """ new(stores the obj into '__objects' using
        <class name>.id as key)
    """
    def new(self, obj):
        """ obj is an object of a class to be
            stored int the '__objects' dictionary
        """
        key = type(self).__name__
        key += "."
        key += obj.id
        FileStorage.__objects[key] = obj

    """ save(stores the '__objects' dictionary in
        a json file)
    """
    def save(self):
        """ stores obj as json file """
        obj = {}
        dict1 = FileStorage.__objects
        for key in dict1.keys():
            obj[key] = dict1[key].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj, f)
    """
    deserializes a json file into a python
    object
    """
    def reload(self):
        """ if the json file doesn't exist,
            the function simply returns
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
                for obj in new_dict.values():
                    cls_name = obj["__class__"]
                    cls_name += "()"
                    del obj["__class__"]
                    instance = eval(cls_name)
                    self.new(instance)
        except FileNotFoundError:
            return
>>>>>>> debe45bea197084243eb8a7cafa0ca410cca13c7

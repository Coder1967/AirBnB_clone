#!/usr/bin/python3
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

#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
""" declaration of a class 'BaseModel' """


class BaseModel:
    """ initialization of instance attributes"""
    def __init__(self, *args, **kwargs):
        """ setting attributes for instance"""
        if (len(kwargs) == 0):
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            l1 = []
            i = 0
            str1 = ""
            str2 = ""
            for k, v in kwargs.items():
                if k != '__class__' and k != 'updated_at':
                    if k != 'created_at':
                        self.__dict__[k] = v

            """ converting strings to datetime objof updated_at"""
            str1 = kwargs['updated_at']

            while i < len(str1):
                if str1[i] == '-' or str1[i] == ':' or str1[i] == 'T':
                    l1.append(int(str2))
                    str2 = ""
                elif str1[i] == '.':
                    l1.append(int(str2))
                    str2 = ""
                else:
                    str2 += str1[i]
                if i == len(str1) - 1:
                    l1.append(int(str2))
                i += 1

            self.updated_at\
                = datetime(l1[0], l1[1], l1[2], l1[3], l1[4], l1[5], l1[6])

            """ converting strings to datetime obj;of updated_at"""
            i = 0
            l1 = []
            str2 = ""
            str1 = kwargs['created_at']
            while i < len(str1):
                if str1[i] == '-' or str1[i] == ':' or str1[i] == 'T':
                    l1.append(int(str2))
                    str2 = ""
                elif str1[i] == '.':
                    l1.append(int(str2))
                    str2 = ""
                else:
                    str2 += str1[i]
                if i == len(str1) - 1:
                    l1.append(int(str2))
                i += 1

            self.created_at\
                = datetime(l1[0], l1[1], l1[2], l1[3], l1[4], l1[5], l1[6])

    """ initialization of the str magic method """
    def __str__(self):
        """ str representation of object """
        return "\
[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    """ initilizing 'save' public method"""
    def save(self):
        """ updates the attr 'updated_at' """
        self.updated_at = datetime.now()
        models.storage.save()

        """ returns a dictionary representation similar to
__dict__ with some additions"""
    def to_dict(self):
        """ defining function to return dict"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

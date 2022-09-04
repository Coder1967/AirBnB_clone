#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime
import os
""" unittests for base_model"""


class Base_test(unittest.TestCase):
    """ beginning tests """
    @classmethod
    def setUp(self):
        """ first method ran, sets up test
        """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    def test_id(self):
        """ beginning test for id"""
        base1 = BaseModel()
        self.assertEqual(base1.id, base1.id)

    """ tests for the created_at object attr"""
    def test_created_at(self):
        """ beginning test for 'created_at'"""
        base1 = BaseModel()
        self.assertAlmostEqual(base1.created_at, base1.created_at)

    """ tests for the updated_at  attr"""
    def test_updated(self):
        """ beginning the tests """
        b1 = BaseModel()
        self.assertAlmostEqual(b1.updated_at, b1.updated_at,)

    """ test for the 'to_dict' function"""
    def test_to_dict(self):
        """ beginning test for 'to_dict func'"""
        base1 = BaseModel()
        diction = base1.to_dict()
        base2 = BaseModel(**diction)
        self.assertEqual(base1.id, base2.id)

    """ test for the 'save' function"""
    def test_save(self):
        """ beginning test for 'save' """
        base1 = BaseModel()
        store = FileStorage()
        update = base1.updated_at
        self.assertEqual(update, base1.updated_at)
        base1.save()
        self.assertNotEqual(update, base1.updated_at)
        store.reload()
        dict1 = base1.__dict__
        dict2 = store.all()
        key = "BaseModel" + "." + base1.id
        dict2 = dict2[key].to_dict()
        del dict2["__class__"]
        self.assertEqual(dict1["id"], dict2['id'])

    def test_kwargs(self):
        """ tests if the key word arguments are used and *args are ignored"""
        b1 = BaseModel()
        kwarg = b1.to_dict()
        b2 = BaseModel("hello", **kwarg)
        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.updated_at, b2.updated_at)
        self.assertEqual(b1.created_at, b2.created_at)

    def test_str(self):
        """ test if the class returns the proper string"""
        bm = BaseModel()
        string = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), string)

    @classmethod
    def tearDown(self):
        """
        last method ran. closes up test
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

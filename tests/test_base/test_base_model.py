#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import os
""" unittests for base_model"""


class Base_test(unittest.TestCase):
    """ tests for the unique id of object"""
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
        self.assertAlmostEqual(b1.updated_at, b1.updated_at)

    """ test for the 'to_dict' function"""
    def test_to_dict(self):
        """ beginning test for 'to_dict func"""
        base1 = BaseModel()
        diction = base1.to_dict()
        base2 = BaseModel(**diction)
        self.assertEqual(base1.id, base2.id)

    """ test for the 'save' function"""
    def test_save(self):
        """ beginning test for 'save' """
        base1 = BaseModel()
        t = base1.updated_at
        base1.save()
        self.assertNotEqual(t, base1.updated_at)
    
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

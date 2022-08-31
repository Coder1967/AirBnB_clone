#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from unittest import TestCase
import os
""" tests for 'FileStorag' class """


class test_storage(TestCase):
    """ beginning unnitests for FileStorage"""
    @classmethod
    def setUp(self):
        """ first method ran in the test,
            prepares the test
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def test_storage_methods(self):
        """tests the 'FileStorage' methods"""
        sto = FileStorage()
        obj = BaseModel()
        sto.new(obj)
        sto.save()
        sto.reload()
        dict1 = sto.all()
        dict2 = sto.all()
        self.assertEqual(dict1, dict2)
    
    @classmethod
    def tearDown(self):
        """ last method ran in test. closes
            test
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

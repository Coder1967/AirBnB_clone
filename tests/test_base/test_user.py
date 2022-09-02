#!/usr/bin/python3
""" unnitests for the user module """
from unittest import TestCase
import os
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(TestCase):
    """ neginning unittests """
    @classmethod
    def setUp(self):
        """ first method ran, sets up test
        """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    def test_attr(self):
        """ checks if the public attr were properly assigned"""
        usr = User()
        usr.email = "ex@gmail.com"
        usr.first_name = "nosa"
        usr.last_name = "aghedo"
        usr.password = "password"
        self.assertEqual(usr.email, "ex@gmail.com")
        self.assertEqual(usr.first_name, "nosa")
        self.assertEqual(usr.last_name, "aghedo")
        self.assertEqual(usr.password, "password")

    """ test for the 'save' and 'to_dict' methods
    """
    def test_save_and_to_dict(self):
        """ beginning test for 'save' """
        usr1 = User()
        store = FileStorage()
        usr1.save()
        store.reload()
        dict1 = usr1.__dict__
        dict2 = store.all()
        key = "User" + "." + usr1.id
        dict2 = dict2[key].to_dict()
        self.assertEqual(dict1["id"], dict2['id'])

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

#!/usr/bin/python3
""" unnitests for the user module """
from unittest import TestCase
import os
from models.user import User
from models.base_model import BaseModel
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

    def test_email(self):
        """ checks if the email public attr was properly assigned"""
        User.email = "ex@gmail.com"
        self.assertEqual(User.email, "ex@gmail.com")

    def test_first_name(self):
        """ checks if the first_name public attr was properly assigned"""
        User.first_name = "nosa"
        self.assertEqual(User.first_name, "nosa")

    def test_last_name(self):
        """ checks if the last_name public attr was properly assigned"""
        User.last_name = "aghedo"
        self.assertEqual(User.last_name, "aghedo")

    def test_password(self):
        """ checks if the password public attr was properly assigned"""
        User.password = "password"
        self.assertEqual(User.password, "password")

    """ test for the 'save' method
    """
    def test_save(self):
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

    def test_str(self):
        """ tests string representation"""
        usr = User()
        string = "[User] ({}) {}".format(usr.id, usr.__dict__)
        self.assertEqual(str(usr), string)

    def test_to_dict(self):
        """ tests the to_dict function """
        usr = User()
        dictionary = usr.to_dict()

        usr2 = User(**dictionary)
        self.assertEqual(usr.id, usr2.id)
        self.assertEqual(type(usr), type(usr2))

    def test_issubclass(self):
        """ tests if User is a subclass of BaseModel"""
        usr = User()
        self.assertIsInstance(usr, BaseModel)

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

if __name__ == "__main__":
    unittest.main()

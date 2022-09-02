#!/usr/bin/python3
""" unnitests for the user module """
from unittest import TestCase
import os
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(TestCase):
    """ beginning unittests """
    @classmethod
    def setUp(self):
        """ first method ran, sets up test
        """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    def test_attr(self):
        """
        testing assignment of attributes
        """
        amty = Amenity()
        amty.name = "pool"
        self.assertEqual(amty.name, "pool")

    """ test for the 'save' and 'to_dict' met
    ods
    """
    def test_save_and_to_dict(self):
        """ beginning test for 'save' """
        amnty = Amenity()
        store = FileStorage()
        amnty.save()
        store.reload()
        dict1 = amnty.__dict__
        dict2 = store.all()
        key = "Amenity" + "." + amnty.id
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

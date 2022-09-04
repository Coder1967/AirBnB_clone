#!/usr/bin/python3
""" unnitests for the user module """
from unittest import TestCase
import os
from models.state import State
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(TestCase):
    """ beginning unittests """
    @classmethod
    def setUp(self):
        """ first method ran, sets up test
        """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    def test_state_id(self):
        """ testing the assignments of the state_id public attr """
        state1 = State()
        state1.name = "Edo"
        City.state_id = state1.id

        self.assertEqual(City.state_id, state1.id)

    def test_name(self):
        """ testing the assignment of the name public attr """
        City.name = "Benin"
        self.assertEqual(City.name, "Benin")

    """test for the 'save' and 'to_dict'
    methods
    """
    def test_save_and_to_dict(self):
        """ beginning test for 'save' """
        city1 = City()
        store = FileStorage()
        city1.save()
        store.reload()
        dict1 = city1.__dict__
        dict2 = store.all()
        key = "City" + "." + city1.id
        dict2 = dict2[key].to_dict()
        self.assertEqual(dict1["id"], dict2['id'])

    def test_is_subclass(self):
        """ tests if City is a subclass of BaseModel """
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_str(self):
        """ tests if the proper string representation is returned """
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))

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

#!/usr/bin/python3
""" unnitests for the user module """
from unittest import TestCase
import os
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestPlace(TestCase):
    """ beginning unittests """
    @classmethod
    def setUp(self):
        """
        first method ran, sets up test
        """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    def test_attrs(self):
        """ tests assignemt of attributes"""
        usr1 = User()
        amnty1 = Amenity()
        amnty2 = Amenity()
        city1 = City()
        Place.city_id = city1.id
        Place.user_id = usr1.id
        Place.name = "peak's mansion"
        Place.description = "describing"
        Place.number_rooms = 8
        Place.number_bathrooms = 5
        Place.max_guest = 8
        Place.price_by_night = 2000
        Place.longitude = 56.9
        Place.latitude = 65.0
        Place.amenity_ids = [amnty1.id, amnty2.id]
        self.assertEqual(Place.city_id, city1.id)
        self.assertEqual(Place.user_id, usr1.id)
        self.assertEqual(Place.name, "peak's mansion")
        self.assertEqual(Place.description, "describing")
        self.assertEqual(Place.number_rooms, 8)
        self.assertEqual(Place.number_bathrooms, 5)
        self.assertEqual(Place.max_guest, 8)
        self.assertEqual(Place.price_by_night, 2000)
        self.assertEqual(Place.longitude, 56.9)
        self.assertEqual(Place.latitude, 65.0)
        self.assertEqual(Place.amenity_ids, [amnty1.id, amnty2.id])

    def test_save_and_to_dict(self):
        """ beginning test for 'save' """
        place = Place()
        store = FileStorage()
        place.save()
        store.reload()
        dict1 = place.__dict__
        dict2 = store.all()
        key = "Place" + "." + place.id
        dict2 = dict2[key].to_dict()
        self.assertEqual(dict1["id"], dict2['id'])

    def test_str(self):
        """ to test if the proper str representation is returned"""
        place1 = Place()
        string = "[Place] ({}) {}".format(place1.id, place1.__dict__)
        self.assertEqual(string, str(place1))

    def test_isSubclass(self):
        """ tests if Place is a subclass of BaseModel"""
        place1 = Place()
        self.assertIsInstance(place1, BaseModel)

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

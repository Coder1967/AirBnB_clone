#!/usr/bin/python3
""" unnitests for the user module """
from unittest import TestCase
import os
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.city import City
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
        place1 = Place()
        usr1 = User()
        amnty1 = Amenity()
        amnty2 = Amenity()
        city1 = City()
        place1.city_id = city1.id
        place1.user_id = usr1.id
        place1.name = "peak's mansion"
        place1.description = "describing"
        place1.number_rooms = 8
        place1.number_bathrooms = 5
        place1.max_guest = 8
        place1.price_by_night = 2000
        place1.longitude = 56.9
        place1.latitude = 65.0
        place1.amenity_ids = [amnty1.id, amnty2.id]
        self.assertEqual(place1.city_id, city1.id)
        self.assertEqual(place1.user_id, usr1.id)
        self.assertEqual(place1.name, "peak's mansion")
        self.assertEqual(place1.description, "describing")
        self.assertEqual(place1.number_rooms, 8)
        self.assertEqual(place1.number_bathrooms, 5)
        self.assertEqual(place1.max_guest, 8)
        self.assertEqual(place1.price_by_night, 2000)
        self.assertEqual(place1.longitude, 56.9)
        self.assertEqual(place1.latitude, 65.0)
        self.assertEqual(place1.amenity_ids, [amnty1.id, amnty2.id])

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

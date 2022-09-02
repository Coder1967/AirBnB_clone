#!/usr/bin/python3
""" unnitests for the user module """
from unittest import TestCase
import os
from models.user import User
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(TestCase):
    """ neginning unittests """
    @classmethod
    def setUp(self):
        """ first method ran, sets up test
        """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
    
    def test_attrs(self):
        """ testing attribute assignment """
        place = Place()
        review = Review
        usr = User()
        review.place_id = place.id
        review.user_id = usr.id
        review.text = "it was a splendid stay. 5 *"
        self.assertEqual(review.place_id, place.id)
        self.assertEqual(review.user_id, usr.id)
        self.assertEqual(review.text, "it was a splendid stay. 5 *")
    
    """ test for the 'save' and 'to_dict' metods 
    """
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
        """ closes up the tests"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

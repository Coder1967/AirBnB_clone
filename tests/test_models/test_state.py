#!/usr/bin/python3
""" unnitests for the state module """
from unittest import TestCase
import os
from models.state import State
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestUser(TestCase):
    """ beginning unittests """
    @classmethod
    def setUp(self):
        """ first method ran, sets up test
        """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    def test_name_attr(self):
        """ testing assignmen of attr "name"
        """
        state1 = State()
        state1.name = "edo"
        self.assertEqual(state1.name, "edo")

    def test_str(self):
        """ tests if the proper string representation is returned """
        st = State()
        string = "[State] ({}) {}".format(st.id, st.__dict__)
        self.assertEqual(string, str(st))

    def test_is_instance(self):
        st = State()
        self.assertIsInstance(st, BaseModel)

    """ test for the 'save' and 'to_dict'
    metods
    """
    def test_save_and_to_dict(self):
        """ beginning test for 'save' """
        state1 = State()
        store = FileStorage()
        state1.save()
        store.reload()
        dict1 = state1.__dict__
        dict2 = store.all()
        key = "State" + "." + state1.id
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

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test state_id attribute to be an empty string """
        new = self.value()
        self.assertTrue(hasattr(new, "state_id"))
        self.assertEqual(new.state_id, None)

    def test_name(self):
        """ Test name attribute to be an empty string"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(new.name, None)

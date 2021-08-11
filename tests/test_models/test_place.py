#!/usr/bin/python3
""" Test the Place class """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test city_id attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "city_id"))
        self.assertEqual(new.city_id, None)

    def test_user_id(self):
        """ Test user_id attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(new.user_id, None)

    def test_name(self):
        """ Test name attribute is empty"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(new.name, None)

    def test_description(self):
        """ Test description attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "description"))
        self.assertEqual(new.description, None)

    def test_number_rooms(self):
        """ Test number_rooms attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "number_rooms"))
        self.assertEqual(new.number_rooms, None)

    def test_number_bathrooms(self):
        """ Test number_bathrooms attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "number_bathrooms"))
        self.assertEqual(new.number_bathrooms, None)

    def test_max_guest(self):
        """ Test max_guest attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "max_guest"))
        self.assertEqual(new.max_guest, None)

    def test_price_by_night(self):
        """ Test price_by_night attribute is empty"""
        new = self.value()
        self.assertTrue(hasattr(new, "price_by_night"))
        self.assertEqual(new.price_by_night, None)

    def test_latitude(self):
        """ Test latitude attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "latitude"))
        self.assertEqual(new.latitude, None)

    def test_longitude(self):
        """ Test longitude attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "longitude"))
        self.assertEqual(new.latitude, None)

    def test_amenity_ids(self):
        """ Test amenity_ids attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "amenity_ids"))
        self.assertEqual(type(new.amenity_ids), list)

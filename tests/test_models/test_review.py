#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ Initialize class for testing """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test place_id attribute to be an empty string"""
        new = self.value()
        self.assertTrue(hasattr(new, "place_id"))
        self.assertEqual(new.place_id, None)

    def test_user_id(self):
        """ Test user_id attribute to be an empty string"""
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(new.user_id, None)

    def test_text(self):
        """ Test text attribute to be an empty string"""
        new = self.value()
        self.assertTrue(hasattr(new, "text"))
        self.assertEqual(new.text, None)

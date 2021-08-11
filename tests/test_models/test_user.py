#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test first_name attribute is empty"""
        new = self.value()
        self.assertTrue(hasattr(new, "first_name"))
        self.assertEqual(new.first_name, None)

    def test_last_name(self):
        """ Test last_name attribute is empty"""
        new = self.value()
        self.assertTrue(hasattr(new, "last_name"))
        self.assertEqual(new.last_name, None)

    def test_email(self):
        """ Test email attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "email"))
        self.assertEqual(new.email, None)

    def test_password(self):
        """ Test password attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "password"))
        self.assertEqual(new.password, None)

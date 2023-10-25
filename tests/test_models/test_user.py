#!/usr/bin/python3
"""
Unit tests for the User class
"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User

class TestUser(test_basemodel):
    """
    Test class for the User model
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes TestUser
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Test first_name attribute type
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Test last_name attribute type
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Test email attribute type
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Test password attribute type
        """
        new = self.value()
        self.assertEqual(type(new.password), str)

#!/usr/bin/python3
"""
Unit tests for the Review class
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review

class TestReview(test_basemodel):
    """
    Test class for the Review model
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes TestReview
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Test place_id attribute type
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Test user_id attribute type
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Test text attribute type
        """
        new = self.value()
        self.assertEqual(type(new.text), str)


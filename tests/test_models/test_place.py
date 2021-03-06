#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Class to test Place"""

    def test_types(self):
        """test attribute types and class type"""
        model1 = Place()
        self.assertEqual(type(model1), Place)
        self.assertEqual(type(model1.id), str)
        self.assertEqual(type(model1.created_at), datetime)
        self.assertEqual(type(model1.updated_at), datetime)
        self.assertEqual(type(model1.city_id), str)
        self.assertEqual(type(model1.user_id), str)
        self.assertEqual(type(model1.name), str)
        self.assertEqual(type(model1.description), str)
        self.assertEqual(type(model1.number_rooms), int)
        self.assertEqual(type(model1.number_bathrooms), int)
        self.assertEqual(type(model1.max_guest), int)
        self.assertEqual(type(model1.price_by_night), int)
        self.assertEqual(type(model1.latitude), float)
        self.assertEqual(type(model1.longitude), float)
        self.assertEqual(type(model1.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()

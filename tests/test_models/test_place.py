#!/usr/bin/python3
"""
Module of the City unittest
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import pep8
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test of the Place class
    """


    #Specific set up of the unittest
    @classmethod
    def SetUp(cls):
        """Instance of the class"""
        cls.inst = Place()

    @classmethod
    def Teardown(cls):
        """Deleting of the instance with the proper file"""
        del cls.inst

        try:
            os.remove("file.json")
        except BaseException:
            pass


    #Functionality
    def TestAtributtesClass(self):
        self.inst.name = "Nicolas"
        self.assertEqual("Nicolas", self.inst.name)
        self.assertEqual(str, type(self.inst.city_id))
        self.assertEqual(str, type(self.inst.user_id))
        self.assertEqual(str, type(self.inst.name))
        self.assertEqual(str, type(self.inst.description))
        self.assertEqual(int, type(self.inst.number_rooms))
        self.assertEqual(int, type(self.inst.number_bathrooms))
        self.assertEqual(int, type(self.inst.max_guest))
        self.assertEqual(int, type(self.inst.price_by_night))
        self.assertEqual(float, type(self.inst.latitude))
        self.assertEqual(float, type(self.inst.longitude))
        self.assertEqual(list, type(self.inst.amenity_ids))


    #Documentation
    def TestModuleDocstring(self):
        """Testing the documentation of the module"""
        self.assertIsNotNone(Place.__doc__)

    def TestMethodsDocstring(self):
        """Testing the documentation of the different methods"""
        for doc in dir(Place):
            self.assertIsNotNone(doc.__doc__)


    #Existence and types
    def TestIsInstance(self):
        """Testing the existence of the instance"""
        self.assertIsInstance(self.inst, Place)

    def TestTypeId(self):
        """Test the type of the method id"""
        self.assertEqual(str, type(self.inst.id))

    def TestFile(self):
        """The existence of the json file"""
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def TestMethods(self):
        """Testing the existence of the different methods"""
        self.assertTrue(hasattr(Place, "__init__"))
        self.assertTrue(hasattr(Place, "__str__"))
        self.assertTrue(hasattr(Place, "save"))
        self.assertTrue(hasattr(Place, "to_dict"))

    def TestClassDict(self):
        """Testing the dictionary of the class"""
        ClassDict = self.inst.to_dict()
        self.assertEqual(dict, type(dict_test))
        self.assertIsInstance(ClassDict["created_at"], str)
        self.assertIsInstance(ClassDict["updated_at"], str)
        self.assertTrue("ClassDict" in dir(self.inst))
        self.assertEqual(Classict.__class_.__name__, "Place")

if __name__ == "__main__":
    unittest.main()

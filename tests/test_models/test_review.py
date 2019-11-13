#!/usr/bin/python3
"""
Module of the Review unittest
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import pep8
from models.review import review


class TestReview(unittest.TestCase):
    """
    Test of the Review class
    """


    #Specific set up of the unittest
    @classmethod
    def SetUp(cls):
        """Instance of the class"""
        cls.inst = Review()

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
        self.assertEqual(str, type(self.inst.place_id))
        self.assertEqual(str, type(self.inst.user_id))
        self.assertEqual(str, type(self.inst.text))


    #Documentation
    def TestModuleDocstring(self):
        """Testing the documentation of the module"""
        self.assertIsNotNone(Review.__doc__)

    def TestMethodsDocstring(self):
        """Testing the documentation of the different methods"""
        for doc in dir(Review):
            self.assertIsNotNone(doc.__doc__)


    #Existence and types
    def TestIsInstance(self):
        """Testing the existence of the instance"""
        self.assertIsInstance(self.inst, Review)

    def TestTypeId(self):
        """Test the type of the method id"""
        self.assertEqual(str, type(self.inst.id))

    def TestFile(self):
        """The existence of the json file"""
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def TestMethods(self):
        """Testing the existence of the different methods"""
        self.assertTrue(hasattr(Review, "__init__"))
        self.assertTrue(hasattr(Review, "__str__"))
        self.assertTrue(hasattr(Review, "save"))
        self.assertTrue(hasattr(Review, "to_dict"))

    def TestClassDict(self):
        """Testing the dictionary of the class"""
        ClassDict = self.inst.to_dict()
        self.assertEqual(dict, type(dict_test))
        self.assertIsInstance(ClassDict["created_at"], str)
        self.assertIsInstance(ClassDict["updated_at"], str)
        self.assertTrue("ClassDict" in dir(self.inst))
        self.assertEqual(Classict.__class_.__name__, "Amenity")

if __name__ == "__main__":
    unittest.main()

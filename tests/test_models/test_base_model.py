#!/usr/bin/python3
"""
Module of the BaseModel unittest
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import pep8


class TestBaseModel(unittest.TestCase):
    """
    Test of the BaseModel class
    """


    #Specific set up of the unittest
    @classmethod
    def SetUp(cls):
        """Instance of the class"""
        cls.inst = BaseModel()

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
        self.inst.name = "Diego"
        self.inst.number = 19
        self.inst.place = "San Francisco"
        self.inst.number_rooms = 1
        self.assertEqual(str, type(self.inst.name))
        self.assertEqual(int, type(self.inst.number))
        self.assertEqual(str, type(self.inst.place))
        self.assertEqual(int, type(self.inst.number_rooms))
        self.assertEqual(datetime.now(), self.inst.created_at)
        self.assertEqual(datetime.now(), self.inst.updated_at)


    #Documentation
    def TestModuleDocstring(self):
        """Testing the documentation of the module"""
        self.assertIsNotNone(BaseModel.__doc__)

    def TestMethodsDocstring(self):
        """Testing the documentation of the different methods"""
        for doc in dir(BaseModel):
            self.assertIsNotNone(doc.__doc__)


    #Existence and types
    def TestIsInstance(self):
        """Testing the existence of the instance"""
        self.assertIsInstance(self.inst, BaseModel)

    def TestTypeId(self):
        """Test the type of the method id"""
        self.assertEqual(str, type(self.inst.id))

    def TestFile(self):
        """The existence of the json file"""
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def TestMethods(self):
        """Testing the existence of the different methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def TestClassDict(self):
        """Testing the dictionary of the class"""
        ClassDict = self.inst.to_dict()
        self.assertIsInstance(ClassDict["created_at"], str)
        self.assertIsInstance(ClassDict["updated_at"], str)
        self.assertTrue("ClassDict" in dir(self.inst))
        self.assertEqual(test_dict.__class_.__name__, "BaseModel")

if __name__ == "__main__":
    unittest.main()

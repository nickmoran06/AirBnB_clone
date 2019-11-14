#!/usr/bin/python3
"""
Module of the BaseModel unittest
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """
    Test of the BaseModel class
    """


    #Specific set up of the unittest
    def setUp(self):
        """Instance of the class"""
        self.inst = BaseModel()

    def tearDown(self):
        """Deleting of the instance with the proper file"""
        del self.inst

        try:
            os.remove("file.json")
        except BaseException:
            pass


    #Functionality
    def test_AtributtesClass(self):
        self.inst.name = "Diego"
        self.inst.number = 19
        self.inst.place = "San Francisco"
        self.inst.number_rooms = 1
        self.assertEqual(str, type(self.inst.name))
        self.assertEqual(int, type(self.inst.number))
        self.assertEqual(str, type(self.inst.place))
        self.assertEqual(int, type(self.inst.number_rooms))
        self.assertNotEqual(datetime.now(), self.inst.created_at)
        self.assertNotEqual(datetime.now(), self.inst.updated_at)


    #Documentation
    def test_ModuleDocstring(self):
        """Testing the documentation of the module"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_MethodsDocstring(self):
        """Testing the documentation of the different methods"""
        for doc in dir(BaseModel):
            self.assertIsNotNone(doc.__doc__)


    #Existence and types
    def test_IsInstance(self):
        """Testing the existence of the instance"""
        self.assertIsInstance(self.inst, BaseModel)

    def test_TypeId(self):
        """Test the type of the method id"""
        self.assertEqual(str, type(self.inst.id))

    def test_File(self):
        """The existence of the json file"""
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_Methods(self):
        """Testing the existence of the different methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_ClassDict(self):
        """Testing the dictionary of the class"""
        ClassDict = self.inst.to_dict()
        self.assertIsInstance(ClassDict["created_at"], str)
        self.assertIsInstance(ClassDict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()

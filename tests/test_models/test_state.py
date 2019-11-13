#!/usr/bin/python3
"""
Module of the State unittest
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import pep8
from models.state import State


class TestState(unittest.TestCase):
    """
    Test of the State class
    """


    #Specific set up of the unittest
    @classmethod
    def SetUp(cls):
        """Instance of the class"""
        cls.inst = State()

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
        self.assertEqual(str, type(self.inst.name))
        self.assertEqual("Nicolas", self.inst.name)


    #Documentation
    def TestModuleDocstring(self):
        """Testing the documentation of the module"""
        self.assertIsNotNone(State.__doc__)

    def TestMethodsDocstring(self):
        """Testing the documentation of the different methods"""
        for doc in dir(State):
            self.assertIsNotNone(doc.__doc__)


    #Existence and types
    def TestIsInstance(self):
        """Testing the existence of the instance"""
        self.assertIsInstance(self.inst, State)

    def TestTypeId(self):
        """Test the type of the method id"""
        self.assertEqual(str, type(self.inst.id))

    def TestFile(self):
        """The existence of the json file"""
        self.inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def TestMethods(self):
        """Testing the existence of the different methods"""
        self.assertTrue(hasattr(State, "__init__"))
        self.assertTrue(hasattr(State, "__str__"))
        self.assertTrue(hasattr(State, "save"))
        self.assertTrue(hasattr(State, "to_dict"))

    def TestClassDict(self):
        """Testing the dictionary of the class"""
        ClassDict = self.inst.to_dict()
        self.assertEqual(dict, type(dict_test))
        self.assertIsInstance(ClassDict["created_at"], str)
        self.assertIsInstance(ClassDict["updated_at"], str)
        self.assertTrue("ClassDict" in dir(self.inst))
        self.assertEqual(Classict.__class_.__name__, "State")

if __name__ == "__main__":
    unittest.main()

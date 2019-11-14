#!/usr/bin/python3
"""
Module that contains the class BaseModel
"""

import models
from datetime import datetime
import uuid

date = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel is the base class of the project
    """

    def __init__(self, *args, **kwargs):
        """Initialization of the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, date))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """String representation of the class"""
        return "[{:s}] ({:s}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        cpy_dict = self.__dict__.copy()
        cpy_dict["__class__"] = self.__class__.__name__
        cpy_dict["created_at"] = cpy_dict["created_at"].strftime(date)
        cpy_dict["updated_at"] = cpy_dict["updated_at"].strftime(date)
        return cpy_dict

#!/usr/bin/python3
"""
Module with the user class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Representation of the User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

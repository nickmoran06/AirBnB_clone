#!/usr/bin/python3
"""
Module with the Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review representation
    """

    place_id = ""
    user_id = ""
    text = ""

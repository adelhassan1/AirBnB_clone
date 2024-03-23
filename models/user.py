#!/usr/bin/python3
"""
Module User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from BaseModel
    Public class attributes:
        email:          (str)
        password:       (str)
        first_name:     (str)
        last_name:      (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

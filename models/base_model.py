#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

"""
Module BaseModel
Defines all classes
"""


class BaseModel():
    """Base class for Airbinb project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """Initialize attributes: uuid, create/update date.
        Args:
            *args
            **kwargs
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(
                            val, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                            val, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, val)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return string of information about Model
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns dic containing all keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                my_dict[k] = v.isoformat()
            else:
                my_dict[k] = v
        return my_dict

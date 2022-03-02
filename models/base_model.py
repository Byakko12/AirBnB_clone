#!/usr/bin/python3
"""
Base model class
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    init attributes
    """

    def __init__(self):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        to_dict = dict(self.__dict__)
        to_dict[__class__] = self.__class__.__name__
        to_dict['created_at'] = self.created_at.isoformat()
        to_dict['update_at'] = self.updated_at.isoformat()
        return to_dict

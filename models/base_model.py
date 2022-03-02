#!/usr/bin/python3
"""
Base model class
"""

from datetime import datetime
import uuid
import models

class BaseModel:
    """
    init attributes
    """

    def __init__(self, *args, **kwargs):

        if kwargs and len(kwargs) != 0:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.created_at = datetime.strptime(
                self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(
                self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        return "[{:s}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        
        #dict1 = dict(self.__dict__)
        #dict1['__class__'] = self.__class__.__name__
        #dict1.update({'created_at': self.created_at.isoformat(),
        #               'updated_at': self.updated_at.isoformat()})
        #return dict1
        dict1 = self.__dict__.copy()
        dict1['__class__'] = self.__class__.__name__
        dict1['created_at'] = self.created_at.isoformat()
        dict1['updated_at'] = self.updated_at.isoformat()
        
        return dict1

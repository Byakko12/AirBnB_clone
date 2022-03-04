#!/usr/bin/python3
"""
Create user inherits BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class attribute"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

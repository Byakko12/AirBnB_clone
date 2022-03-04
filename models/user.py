#!/usr/bin/python3

"""
Create user inherits BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    

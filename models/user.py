#!/usr/bin/python3
from models.base_model import BaseModel
""" definition of the class 'User' """


class User(BaseModel):
    """ public classes to store the email, name, first and last
        name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

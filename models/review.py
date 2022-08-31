#!/usr/bin/python3
from models.base_model import BaseModel
""" definition of class 'Review' """


class Review(BaseModel):
    """
    place_id(it will be the Place.id)
    user_id( it will be the User.id)
    text(the review)
    """
    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel
from os import getenv


class Amenity(BaseModel):
    """Representation of Amenity """
    name = ""

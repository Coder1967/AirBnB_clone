#!/usr/bin/python3
"""
initialize the models package
"""
from models.engine.file_storage import FileStorage
""" creating a FileStorage object
"""
storage = FileStorage()
storage.reload()

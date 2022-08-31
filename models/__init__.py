#!/usr/bin/python3
<<<<<<< HEAD
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
=======
from models.engine.file_storage import FileStorage
""" creating a FileStorage object
"""
storage = FileStorage()
>>>>>>> debe45bea197084243eb8a7cafa0ca410cca13c7
storage.reload()

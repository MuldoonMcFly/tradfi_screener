

#  Contains all the functions needed for this module

import os
from databases.constants import dbname


#  Finds the path of the database
def dbpath():
    path = os.path.dirname(os.path.abspath(__file__))
    db = os.path.join(path, dbname)
    return db


# print(dbpath())



# Calls all the functions and constants needed for this module. This file should be called by main.py.

import sqlite3 as sql
from databases.helpers import dbpath


# Functions to help interact with the database


db_conn = sql.connect(dbpath())


db_curs = db_conn.cursor()

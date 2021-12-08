import sqlite3
class DatabaseHelper:
    connection = None
    def __init__(self):
        connection = sqlite3.connect('database.db')
       
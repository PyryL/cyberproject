import sqlite3
import os
import hashlib

# clear any existing database
try:
    os.remove("database.db")
except FileNotFoundError:
    pass

# create new empty database
from db import connection
cursor = connection.cursor()

# format the database according to schema
with open("schema.sql", "r") as file:
    cursor.executescript(file.read())

# insert example users
hash = lambda s : hashlib.md5(s.encode("utf-8")).hexdigest()
users = [
    ("janedoe", hash("password")),
    ("johndoe", hash("secret")),
]
cursor.executemany("INSERT INTO Users (username, passwd) VALUES (?, ?)", users)

# insert example todos
todos = [
    (1, "buy milk"),
    (2, "learn to code in Swift"),
    (1, "fix flaws in the codebase"),
]
cursor.executemany("INSERT INTO Todos (user, content) VALUES (?, ?)", todos)
connection.commit()

print("Database formatted and example data inserted!")
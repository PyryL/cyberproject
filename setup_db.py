import sqlite3
import os
import hashlib
from utilities.hash import generate_hash

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
users = [
    ("janedoe", generate_hash("password"), ),
    ("johndoe", generate_hash("secret"), ),
]
cursor.executemany("INSERT INTO Users (username, passwd) VALUES (?, ?)", users)

# insert example todos
todos = [
    (1, "buy milk"),
    (2, "learn to code in Swift"),
    (1, "fix flaws in the codebase"),
    (100, "hack a website<script>setTimeout(() => alert('hacked!'), 750)</script>"),
]
cursor.executemany("INSERT INTO Todos (user, content) VALUES (?, ?)", todos)
connection.commit()

print("Database formatted and example data inserted!")

from db import connection
from utilities.hash import generate_hash, check_hash

class Users:
    @classmethod
    def create_new_user(cls, username: str, password: str):
        cursor = connection.cursor()

        # check for duplicate username
        sql = "SELECT COUNT(*) FROM Users WHERE username=?"
        result = cursor.execute(sql, (username, )).fetchone()
        if result[0] != 0:
            return False

        sql = "INSERT INTO Users (username, passwd) VALUES (?, ?)"
        cursor.execute(sql, (username, generate_hash(password), ))
        connection.commit()
        return True

    @classmethod
    def validate_credentials(cls, username: str, password: str) -> int:
        cursor = connection.cursor()
        sql = "SELECT id, passwd FROM Users WHERE username=?"
        result = cursor.execute(sql, (username, )).fetchone()
        if result is None or not check_hash(password, result[1]):
            return None
        return result[0]

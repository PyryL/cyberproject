from db import connection
from utilities.hash import check_hash

class Users:
    @classmethod
    def validate_credentials(cls, username: str, password: str) -> int:
        cursor = connection.cursor()
        sql = "SELECT id, passwd FROM Users WHERE username=?"
        result = cursor.execute(sql, (username, )).fetchone()
        if result is None or not check_hash(password, result[1]):
            return None
        return result[0]

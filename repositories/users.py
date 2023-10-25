from db import connection
import hashlib

class Users:
    @classmethod
    def _hash(cls, s: str) -> str:
        return hashlib.md5(s.encode("utf-8")).hexdigest()

    @classmethod
    def validate_credentials(cls, username: str, password: str) -> int:
        cursor = connection.cursor()
        values = (username, Users._hash(password), )
        sql = "SELECT id FROM Users WHERE username=? AND passwd=?"
        result = cursor.execute(sql, values).fetchone()
        if result is None:
            return None
        return result[0]

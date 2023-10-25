from db import connection

class Todos:
    @classmethod
    def get_user_todos(cls, user_id: int) -> list:
        cursor = connection.cursor()
        sql = "SELECT id, content FROM Todos WHERE user=?"
        return [
            { "id": item[0], "content": item[1] }
            for item in cursor.execute(sql, (user_id, )).fetchall()
        ]

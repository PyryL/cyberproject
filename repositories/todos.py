from db import connection

class Todos:
    @classmethod
    def get_user_todos(cls, user_id: int) -> list:
        cursor = connection.cursor()
        # INTENTIONAL VULNERABILITY
        # inserting the parameter to the statement ourselves makes SQL injections possible
        sql = f"SELECT id, content FROM Todos WHERE user={user_id}"
        result = cursor.execute(sql).fetchall()
        # FIX (comment vulnerable code above and uncomment code block below)
        # sql = "SELECT id, content FROM Todos WHERE user=?"
        # result = cursor.execute(sql, (user_id, )).fetchall()

        return [
            { "id": item[0], "content": item[1] }
            for item in result
        ]

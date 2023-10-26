from db import connection

class Todos:
    @classmethod
    def get_user_todos(cls, user_id: int) -> list:
        """Returns the todos owned by the given user as a list of { id, content } dicts."""

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

    @classmethod
    def get_todo_user_id(cls, todo_id: int) -> int:
        """Returns the user ID of the owner of the given todo, or None if not found."""
        cursor = connection.cursor()
        sql = "SELECT user FROM Todos WHERE id=?"
        result = cursor.execute(sql, (todo_id, )).fetchone()
        if result is None:
            return None
        return result[0]

    @classmethod
    def add_todo(cls, content: str, user_id: int):
        """Adds a new todo to database."""
        cursor = connection.cursor()
        sql = "INSERT INTO Todos (user, content) VALUES (?, ?)"
        cursor.execute(sql, (user_id, content, ))
        connection.commit()

    @classmethod
    def delete_todo(cls, todo_id: int):
        """Deletes the given todo from database."""
        cursor = connection.cursor()
        sql = "DELETE FROM Todos WHERE id=?"
        cursor.execute(sql, (todo_id, ))
        connection.commit()

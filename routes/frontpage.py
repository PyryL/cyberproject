from flask import request
from app import app
from repositories.todos import Todos
from utilities.session import Session

@app.route("/")
def frontpage():
    user_id = Session.check_user_id(request)
    html = "<h1>Todo</h1>"
    if user_id is not None:
        user_todos = Todos.get_user_todos(user_id)
        html += "<b>My todos:</b><ul>"
        for item in user_todos:
            html += "<li>" + item["content"] + "</li>"
        html += "</ul>"
    else:
        html += '<a href="/login">Log in</a>'
    return html

from flask import request
from app import app
from utilities.session import Session

@app.route("/")
def frontpage():
    user_id = Session.check_user_id(request)
    return f"<h1>Todo</h1><p>Session user {user_id}</p>"

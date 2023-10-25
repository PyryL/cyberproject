from flask import request, render_template
from app import app
from repositories.todos import Todos
from utilities.session import Session

@app.route("/")
def frontpage():
    user_id = Session.check_user_id(request)
    user_todos = [] if user_id is None else Todos.get_user_todos(user_id)

    # INTENTIONAL VULNERABILITY
    html = "<h1>Todo</h1>"
    if user_id is not None:
        html += "<b>My todos:</b><ul>"
        for item in user_todos:
            # this allows injecting HTML code unsanitized to the webpage
            html += "<li>" + item["content"] + "</li>"
        html += "</ul>"
    else:
        html += '<a href="/login">Log in</a>'
    return html
    # FIX (comment the vulnerable code block above and uncomment the code below)
    # use Jinja framework that automatically sanitizes all input
    # return render_template("frontpage.html",
    #     is_logged_in=user_id is not None,
    #     todos=user_todos)

from flask import request, render_template, abort, redirect
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
            html += f'<li>{item["content"]} <a href="/delete/{item["id"]}">Delete</a></li>'
        html += "</ul>"
    else:
        html += '<a href="/login">Log in</a>'
    return html
    # FIX (comment the vulnerable code block above and uncomment the code below)
    # use Jinja framework that automatically sanitizes all input
    # return render_template("frontpage.html",
    #     is_logged_in=user_id is not None,
    #     todos=user_todos)

@app.route("/delete/<todo_id>")
def deleteTodo(todo_id: int):
    # check that user is logged in
    user_id = Session.check_user_id(request)
    if user_id is None:
        return abort(401)

    # check that user is the owner of this todo
    todo_owner_id = Todos.get_todo_user_id(todo_id)
    if todo_owner_id is None:
        return abort(404)
    if str(todo_owner_id) != str(user_id):
        return abort(403)

    Todos.delete_todo(todo_id)
    return redirect("/")

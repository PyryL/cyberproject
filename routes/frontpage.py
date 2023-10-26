from flask import request, render_template, abort, redirect
from app import app
from repositories.todos import Todos
from utilities.session import Session
from utilities.validation import Validation

@app.route("/")
def frontpage():
    user_id = Session.check_user_id(request)
    user_todos = [] if user_id is None else Todos.get_user_todos(user_id)

    # INTENTIONAL VULNERABILITY
    html = "<h1>Todo</h1>"
    if user_id is not None:
        html += '<p><a href="/logout">Log out</a></p>'
        html += "<b>My todos:</b><ul>"
        for item in user_todos:
            # this allows injecting HTML code unsanitized to the webpage
            html += f'<li>{item["content"]} <form action="/delete/{item["id"]}" method="POST" style="display:inline">'
            html += f'<input type="hidden" name="csrf_token" value="{Session.csrf_token()}">'
            html += f'<input type="submit" value="Delete"></form></li>'
        html += '<li><form action="/add-todo" method="POST"><input name="content" placeholder="New todo">'
        html += f'<input type="hidden" name="csrf_token" value="{Session.csrf_token()}">'
        html += '<input type="submit" value="Add"></form></li>'
        html += "</ul>"
    else:
        html += '<a href="/login">Log in</a>'
    return html
    # FIX (comment the vulnerable code block above and uncomment the code below)
    # use Jinja framework that automatically sanitizes all input
    # return render_template("frontpage.html",
    #     is_logged_in=user_id is not None,
    #     todos=user_todos,
    #     csrf_token=Session.csrf_token())

@app.route("/add-todo", methods=["POST"])
def addTodo():
    user_id = Session.check_user_id(request)
    if user_id is None or request.form.get("csrf_token") != Session.csrf_token():
        return abort(401)

    content = request.form.get("content")
    if not Validation.is_valid_todo_content(content):
        return abort(400)

    Todos.add_todo(content, user_id)
    return redirect("/")

@app.route("/delete/<todo_id>", methods=["POST"])
def deleteTodo(todo_id: int):
    # check that user is logged in
    user_id = Session.check_user_id(request)
    if user_id is None or request.form.get("csrf_token") != Session.csrf_token():
        return abort(401)

    # check that user is the owner of this todo
    todo_owner_id = Todos.get_todo_user_id(todo_id)
    if todo_owner_id is None:
        return abort(404)
    if str(todo_owner_id) != str(user_id):
        return abort(403)

    Todos.delete_todo(todo_id)
    return redirect("/")

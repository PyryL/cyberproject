from flask import render_template, request, redirect
from app import app
from repositories.users import Users

@app.route("/login")
def getLogin():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def postLogin():
    username, password = request.form.get("username"), request.form.get("password")
    user_id = Users.validate_credentials(username, password)
    if user_id is not None:
        return redirect("/login?status=invalid")
    # TODO: set user_id to cookie (intentional vulnerability)
    return redirect("/")

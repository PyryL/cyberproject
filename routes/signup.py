from flask import render_template, redirect, request
from app import app
from repositories.users import Users
from utilities.validation import Validation

@app.route("/signup")
def getSignup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def postSignup():
    username = request.form.get("username")
    password1, password2 = request.form.get("password1"), request.form.get("password2")
    
    if password1 != password2:
        return redirect("/signup?status=mismatch")

    # INTENTIONAL VULNERABILITY
    # no further checks are made to the user input
    # FIX (uncomment the code block below)
    # if not Validation.is_valid_username(username) or not Validation.is_valid_password(password1):
    #     return redirect("/signup?status=weak")

    if not Users.create_new_user(username, password1):
        return redirect("/signup?status=username")

    return redirect("/login?status=signup")

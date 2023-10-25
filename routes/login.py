from flask import render_template
from app import app

@app.route("/login")
def getLogin():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def postLogin():
    return "post login"

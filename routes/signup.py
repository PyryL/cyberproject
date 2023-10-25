from flask import render_template
from app import app

@app.route("/signup")
def getSignup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def postSignup():
    return "post signup"

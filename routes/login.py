from flask import render_template, request, redirect, make_response, session
from app import app
from repositories.users import Users

@app.route("/login")
def getLogin():
    return render_template("login.html", status=request.args.get("status"))

@app.route("/login", methods=["POST"])
def postLogin():
    username, password = request.form.get("username"), request.form.get("password")
    user_id = Users.validate_credentials(username, password)
    if user_id is None:
        return redirect("/login?status=invalid")

    # INTENTIONAL VULNERABILITY
    # user_id is stored plaintext in a cookie
    response = make_response(redirect("/"))
    response.set_cookie("user_id", str(user_id))
    return response
    # FIX (comment vulnerable code above and uncomment this block)
    # store user_id in encrypted session that cannot be tampered by the user
    # session["user_id"] = user_id
    # return redirect("/")

@app.route("/logout")
def logout():
    response = make_response(redirect("/?status=logout"))
    if request.cookies.get("user_id") is not None:
        response.set_cookie("user_id", "", expires=0)       # delete cookie
    else:
        session.pop("user_id", None)
    return response

from app import app

@app.route("/")
def frontpage():
    return "<h1>Todo</h1>"


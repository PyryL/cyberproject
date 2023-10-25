from app import app

@app.route("/")
def frontpage():
    return "Hello, world!"

from app import app

@app.route("/")
def index():
    return "Hello World"

@app.route("/about")
def index():
    return "About page"
from flask import FLASK
app = FLASK(__name__)

@app.route("/", strict_slashes=False)
def hello:
        return "Hello HBNB!$"

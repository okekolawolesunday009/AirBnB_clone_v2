#!/usr/bin/python3
"""start python app
"""
from flask import Flask
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """display states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """display states based on id if any"""
    states = storage.all(State).values()
    for state in states:
        print(state.id)
        if state.id == id:
            print(state.id)
            return render_template(
                    "9-states.html",
                    state=state,
                    )
        return render_template("9-states.html")


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

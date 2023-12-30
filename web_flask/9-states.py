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
    """display states based on id if any"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route("/states/<state_id>", strict_slashes=False)
def states_id(state_id=None):
    """display states based on id if any"""
    states = storage.all(State)
    sel_state = None
    if state_id:
        state_id = 'State.name.' + state_id
        sel_state = states.get(state_id)
        states = [sel_state.to_dict()] if sel_state else []
    return render_template(
            '9-states.html',
            states=states,
            state_id=state_id,
            sel_state=sel_state)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

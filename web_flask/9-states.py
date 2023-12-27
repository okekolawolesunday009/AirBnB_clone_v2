#!/usr/bin/python3
"""start python app
"""
from flask import Flask
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<state_id>", strict_slashes=False)
def states(state_id=None):
    print(state_id)
    """display states based on id if any"""
    states_dict = storage.all(State).items()

    # Check if the state_id includes 'State.' prefix
    if state_id == state.id:
         state = states_dict.get(state_id)
         state_id = state_id
    print(state)
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')


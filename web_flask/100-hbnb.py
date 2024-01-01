#!/usr/bin/python3
"""start python app
"""
from flask import Flask
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    """display states based on id if any"""
    states = storage.all(State).items()
    amenities = storage.all(Amenity).items()
    cities = storage.all(City).items()
    places = storage.all(Place).items()
    print(places)
    return render_template(
            '10-hbnb_filters.html',
            states=states,
            amenities=amenities,
            cities=cities,
            places=places
            )


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')



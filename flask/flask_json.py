from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/likes.json")
def json_data():
    """return some data in json format"""
    favs = {
        "Movie": "Zoolander",
        "Band": "Weezer",
        "Song": "The Middle",
        "Height": 6,
    }
    return jsonify(favs), 200  # use jsonify function, required in flask


# To run, in the terminal:
# export FLASK_APP=flask_hello
# flask run
# can share on the network with flask run --host=0.0.0.0
# to enable debugging - dont use in prod! export FLASK_ENV=development

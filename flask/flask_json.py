from flask import Flask, jsonify


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

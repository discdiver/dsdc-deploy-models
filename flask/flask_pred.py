from flask import Flask, Response, request, jsonify, render_template
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

# initialize the flask app
app = Flask("myApp")


@app.route("/form")
def form():
    """form for getting data"""
    return render_template("form.html")


@app.route("/submit")
def make_predictions():
    """accept form submission and handle it"""

    user_input = request.args

    X_test = np.array(
        [
            int(user_input["OverallQual"]),
            int(user_input["FullBath"]),
            int(user_input["GarageArea"]),
            int(user_input["LotArea"]),
        ]
    ).reshape(1, -1)

    model = pickle.load(open("assets/model.pkl", "rb"))
    pred = model.predict(X_test)
    pred = pred[0]

    return render_template("results.html", prediction=pred)


if __name__ == "__main__":
    app.run()

# To run, in the terminal:
# export FLASK_APP=flask_pred
# flask run
# can share on the network with flask run --host=0.0.0.0
# to enable debugging - dont use in prod! export FLASK_ENV=development

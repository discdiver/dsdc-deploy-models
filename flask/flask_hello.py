from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello friends! 🎉"


# To run, in the terminal:
# export FLASK_APP=flask_hello
# flask run
# can share on the network with flask run --host=0.0.0.0
# to enable debugging - dont use in prod! export FLASK_ENV=development

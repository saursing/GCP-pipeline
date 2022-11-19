#imports
import os
import re
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# initializing Flask app
app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello " + clean_name + "! It's " + formatted_now
    return content

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

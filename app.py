#imports
import os
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy

# initializing Flask app
app = Flask(__name__)

# Google Cloud SQL (change this accordingly)
PASSWORD ="Test#1234"
PUBLIC_IP_ADDRESS ="35.225.130.143"
DBNAME ="Test"
PROJECT_ID ="docker-flask-358409"
INSTANCE_NAME ="gcp-flask-sql1"
Link="mysql+mysqldb://root:Test#1234@35.225.130.143/Test?unix_socket=/cloudsql/docker-flask-358409:gcp-flask-sql1"

# configuration
app.config["SECRET_KEY"] = "yoursecretkey"
app.config["SQLALCHEMY_DATABASE_URI"]= Link
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

db = SQLAlchemy(app)

# User ORM for SQLAlchemy
class Users(db.Model):
  id = db.Column(db.Integer, primary_key = True, nullable = False)
  name = db.Column(db.String(50), nullable = False)
  email = db.Column(db.String(50), nullable = False, unique = True)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

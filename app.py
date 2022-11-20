#imports
import os
import re
import sqlalchemy
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# initializing Flask app
app = Flask(__name__)


connection_name = "rb-munish-playground:us-central1:test-sql"
table_name = "entries"
table_field_1 = "guestName"
table_field_value_1 = "saurabh"
table_field_2 = "content"
table_field_value_2 = "sample test"
db_name = "testing"
db_user = "root"
db_password = "1234"
sql_host="35.192.177.19"
sql_port="3306"

driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})


@app.route('/insert/<request>')
def add(request):
    # getting name and email
    match_object = re.match("name=(.*)&content=(.*)", request)
    name = match_object.group(1)
    content = match_object.group(2)
    stmt = sqlalchemy.text('INSERT INTO entries (guestName, content) values ("{}","{}")'.format(name, content))

    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        host=sql_host,
        port=sql_port,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )
    
    try:
        with db.connect() as conn:
            conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    
    responseObject = {
        'status' : 'success',
        'message': 'Successfully registered.'
    }
 
    return make_response(responseObject, 200)

 
 
@app.route("/viewsql/")
def connect_sql():
    stmt = sqlalchemy.text('SELECT * FROM entries')

    db = sqlalchemy.create_engine(
      sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        host=sql_host,
        port=sql_port,
        database=db_name,
        query=query_string,
      ),
      pool_size=5,
      max_overflow=2,
      pool_timeout=30,
      pool_recycle=1800
    )

    try:
        with db.connect() as conn:
            response = conn.execute(stmt)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    
    output = list()
    for user in response:
        output.append({
            "name" : user.guestName,
            "content": user.content
        })
        
    return make_response({
        'status' : 'success',
        'message': output
    }, 200)
    
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

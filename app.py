from flask import Flask, render_template
import json
import string
import datetime

import mysql.connector
from flask import request
app = Flask(__name__)


# connection mysql
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="node-js"
)

dbCursor = db.cursor()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return form_get_index()
    elif request.method == 'POST':
        fetching = request.json
        sql = 'INSERT INTO users (email , password, email_verified_at) VALUES (%s, %s, %s)'
        value = (fetching['email'], fetching['password'],
                 datetime.datetime.now())
        dbCursor.execute(sql, value)
        db.commit()

        return json.dumps({'message': 'you are insert into databases'})


def form_post_index(request=None):
    return json.dumps(request)


def form_get_index():
    dbCursor.execute("SELECT * FROM users")
    data = dbCursor.fetchall()

    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response

from flask import Flask, render_template, request
from services.db import DBConnection
from helpers.response_person_body import response_person_body
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
    
@app.route("/", methods=["GET"]) #decorador
def index():
    return render_template('index.html')

@app.route("/persons", methods=["POST"]) #decorador
def get_persons():
    active = 1 if request.json["active"] == True else 0
    query = f'INSERT INTO persons VALUES ( {request.json["dni"]}, "{request.json["lastName"]}","{request.json["firstName"]}", {active})'
    print(query)
    db = DBConnection()
    db.excecute_sql(query)
    return request.json, 201

@app.route("/persons/<_id>", methods=["PUT"]) #decorador
def update_persons():
    return {
        "action": "update"
    }

@app.route("/persons/<_id>", methods=["DELETE"]) #decorador
def detele_persons():
    return {
        "action": "delete"
    }


## devuelve solo una persona
@app.route("/persons/<_id>", methods=["GET"]) #decorador
def get_one_persons(_id):
    query = f'SELECT * FROM persons WHERE dni={_id}'
    print(query)
    db = DBConnection()
    db.excecute_sql(query)
    cur = db.get_cursor()
    p = cur.fetchone()
    return response_person_body(p)


## devuelve todas las personas
@app.route("/persons", methods=["GET"]) #decorador
def get_all_persons():
    persons = []
    query = f'SELECT * FROM persons'
    print(query)
    db = DBConnection()
    db.excecute_sql(query)
    cur = db.get_cursor()
    for p in cur.fetchall():
        persons.append(response_person_body(p))   
    return persons, 200

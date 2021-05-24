from flask import Flask, json
from flask import jsonify
from service.persons import lookupPerson,getAllPeople

app = Flask(__name__)

@app.route('/')
def routePage():
    return {
        'routes' : [
            '/people',
            "/people/{id}"
        ]
    }

@app.route("/people")
def getPeople():
    # hardcode filters but will be query params
    hardCodedFilter = {
        'first_name' : '[equals]Malcolm'
    }
    personsList = getAllPeople(hardCodedFilter, None)
    return jsonify(personsList)

@app.route("/people/<int:person_id>")
def getPerson(person_id):
    person = lookupPerson(person_id)
    return {
        'person' : person
    }

from flask import Flask
from datetime import datetime
import re
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return "Hello world flask"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

class TestGet(Resource):
    def get(self, name):
        return {'name': name, 'age': 27}

api.add_resource(TestGet, '/testget/<string:name>')

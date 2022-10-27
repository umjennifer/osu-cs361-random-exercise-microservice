# python3 api.py

from flask import Flask
from flask_restful import Resource, Api
import random
import json

with open('exercises.json') as file:
   exercises_data = json.load(file)

app = Flask(__name__)
api = Api(app)

def generate_prn():
    random.seed()
    len_exercises_data= len(exercises_data)
    index = random.randrange(1, 100)
    if index >= len_exercises_data:
            index = int(index) % len_exercises_data
    return str(index)


class Exercises(Resource):
    def get(self):
        return exercises_data[str(generate_prn())]

api.add_resource(Exercises, '/')

if __name__ == '__main__':
    app.run(debug=True)
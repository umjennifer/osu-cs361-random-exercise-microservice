"""Random Exercise API

Flask Restful API based on
https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api

Main functionality:
- get a random exercise

Other functionality:
- get all exercises
- get an exercise using its ID
- delete an exercise using its ID
- create an exercise
"""

import random
import json
from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

EXERCISES_JSON_FILE = 'exercises.json'
ENCODING = 'utf-8'
with open(EXERCISES_JSON_FILE, encoding=ENCODING) as input_file:
    exercises_data = json.load(input_file)
app = Flask(__name__)
api = Api(app)

def abort_if_exercise_does_not_exist(exercise_id):
    if exercise_id not in exercises_data:
        abort(404, message="Exercise {} doesn't exist".format(exercise_id))

parser = reqparse.RequestParser()
parser.add_argument('exercise')

def write_json_to_file(this_json):
    with open(EXERCISES_JSON_FILE, 'w', encoding=ENCODING) as output_file:
        json.dump(this_json, output_file)


class Exercises(Resource):
    def get(self):
        return exercises_data

    def post(self):
        args = parser.parse_args()
        exercise_id = str(int(max(exercises_data.keys())) + 1)
        exercises_data[exercise_id] = {"name": args['exercise']}
        write_json_to_file(exercises_data)
        return exercises_data[exercise_id]


class Exercise(Resource):
    def get(self, exercise_id):
        abort_if_exercise_does_not_exist(exercise_id)
        return exercises_data[exercise_id]

    def delete(self, exercise_id):
        abort_if_exercise_does_not_exist(exercise_id)
        del exercises_data[exercise_id]
        write_json_to_file(exercises_data)
        return '', 204

    def put(self, exercise_id):
        args = parser.parse_args()
        exercise = {'name': args['exercise']}
        exercises_data[exercise_id] = exercise
        write_json_to_file(exercises_data)
        return exercise, 201


class RandomExercise(Resource):
    def generate_random_key(self):
        random.seed()
        len_exercises_data= len(exercises_data)
        rand_int = random.randrange(0, 1000)

        if rand_int >= len_exercises_data:
            rand_int = int(rand_int) % len_exercises_data

        index_to_key = {}
        for i, key in enumerate(exercises_data.keys()):
            index_to_key[i] = key
        rand_key = index_to_key[rand_int]
        return str(rand_key)

    def get(self):
        return exercises_data[self.generate_random_key()]


api.add_resource(RandomExercise, '/')
api.add_resource(Exercises, '/exercises')
api.add_resource(Exercise, '/exercise/<exercise_id>')


if __name__ == '__main__':
    app.run(debug=True)

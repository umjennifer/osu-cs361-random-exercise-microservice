"""Example: Use Python to call random_exercise_api.py"""

import requests

def call_random_exercise_api(api_url):
    """An example demonstrating how to call the random_exercise_api.py and get a random exercise"

    Args:
        api_url (string): API endpoint for the random_exercise_generator

    Returns:
        json: a key of "name" and a value of the exercise name as a string
    """
    response = requests.get(api_url, timeout=10)
    return response.json()

if __name__ == "__main__":
    # update flask_server_url with site and port where Flask server is running
    FLASK_SERVER_URL = 'http://127.0.0.1:5000'
    API_ENDPOINT = FLASK_SERVER_URL + '/'
    print(call_random_exercise_api(API_ENDPOINT))

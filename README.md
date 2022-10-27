# Random Exercise API

# About
The API returns a JSON containing an exercise randomly chosen from [exercises.json](exercises.json). For example:

```json
{"name": "deadlift"}
```

TODO: UML diagram

# Instructions 

## One-time set-up
1. [Clone the Github repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to your local environment.
    1. In a terminal, navigate to the directory that contains `random_exercise_api.py`.
1. Create a Python virtual environment. In the examples below, we set up a virtual environment called `.venv`

        python3 -m venv .venv

1. Activate the Python virtual environment.

        source .venv/bin/activate

1. Use `pip` to install the dependencies.

        pip install -r requirements.txt

## Request data

Start the Flask API server.
1. In a terminal, navigate to the directory that contains `random_exercise_api.py`.
1. Activate the Python virtual environment from the [One-time Set-Up](#one-time-set-up) section.
1. In the virtual environment, run the following command to start the server.

    ```
    flask --app random_exercise_api.py run
    ```

    <details>
    <summary>Note: Optional Flag(s)</summary>
    - To change the port where the server is running, use the command below:

        ```
        flask --app random_exercise_api.py run -p ${PORT_NUMBER}
        ```

        For example, to run the service on Port 3000:

        ```
        flask --app random_exercise_api.py run -p 3000
        ```
    </details>

1. In the output of the command, you'll find a link to where the server is running. Example:

    ```
    Running on http://127.0.0.1:5000
    ```
    Visit the link to confirm that the server is working. You should see JSON similar to the output below:

    ```
    {"name": "bicep curls"}
    ```

## Receive data
The server will return JSON containing the exercise. For example,

```json
{"name": "deadlift"}
```

Note: In the examples listed, assume the Flask server is running on `http://127.0.0.1:5000`.

### Using a Shell

From a terminal run this command:
```
curl http://127.0.0.1:5000
```

### Using Python
In a Python virtual environment, use the [*requests* module](https://requests.readthedocs.io/en/latest/). Example:

```python
import requests

def call_random_exercise_api(api_url):
    response = requests.get(api_url)
    return(response.json())

if __name__ == "__main__":
    print(call_random_exercise_api('http://127.0.0.1:5000'))  # update input with site and port where Flask server is running
```
This will return output similar to 

```json
{"name": "deadlift"}
```
To get only the value of the JSON (a.k.a the name of the exercise as a string), replace `response.json()` with `response.json()["name"]`

This will return output similar to 

```
deadlift
```

## Add an exercise to the JSON configuration
1. Navigate to [exercises.json](exercises.json).
1. At the end of the file, add a key of the next numerical index and a value of "name": "name_of_exercise". For example:
    
    ```json
    "100": {
        "name": "upright_row"
    }
    ```



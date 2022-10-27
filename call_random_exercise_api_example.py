import requests

def call_random_exercise_api(api_url):
    response = requests.get(api_url)
    return(response.json())

if __name__ == "__main__":
    print(call_random_exercise_api('http://127.0.0.1:5000'))  # update input with site and port where Flask server is running
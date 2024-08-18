import requests
import json

URL = "http://127.0.0.1:8000/api2/student_create/"
data = {
    'name': 'Aarush',
    'roll': 101,
    'city': 'Pokhara',
}

# Convert Python dictionary to JSON string
json_data = json.dumps(data)

# Make the POST request
r = requests.post(url=URL, data=json_data, headers={'Content-Type': 'application/json'})

# Check if the request was successful
if r.status_code == 200:
    # Parse the JSON response
    response_data = r.json()
    print(response_data)
else:
    print(f"Request failed with status code {r.status_code}")
    print(r.text)

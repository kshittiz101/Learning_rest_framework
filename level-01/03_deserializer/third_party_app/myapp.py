import requests
import json

# URL of the API endpoint where the student data will be posted
url = "http://localhost:8000/api/student_create/"  # Replace with the actual URL

# Data to be sent in the POST request (student data)
data = {
    'name': 'Sita Devi',
    'roll': 105,
    'address': '123 Sarlahi'
}

# Convert the Python dictionary to a JSON string
json_data = json.dumps(data)

# Set headers for JSON content type
headers = {
    'Content-Type': 'application/json'
}

# Send POST request with the data and headers
response = requests.post(url, data=json_data, headers=headers)

# Process the response
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.json())

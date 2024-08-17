import requests
print("Enter the id of the student: ")
id = int(input())
URL = f"http://127.0.0.1:8000/api/{id}"
request = requests.get(url=URL)
data = request.json()
print(data)

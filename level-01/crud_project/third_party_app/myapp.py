import requests
import json

URL = "http://127.0.0.1:8000/api/student_api/"

# Get request 
def get_data(id=None): 
    params = {}
    if id is not None:
        params = {'id': id}
    
    r = requests.get(url=URL, params=params)
    
    try:
        data = r.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON")
        print(r.text)  # Print the raw content to understand what went wrong



# create 
def post_data():
    data = {
        'name':'Rahul',
        'roll':105,
        'city':'bara',
    }
    # convert dict into json 
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    try:
        data = r.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON")
        print(r.text)  # Print the raw content to understand what went wrong



# update function 
def update_data():
    data = {
        'id':2,
        'name':'Arjun Shrestha',
        'city':'New Delhi',
    }
    # convert dict into json 
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    try:
        data = r.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON")
        print(r.text) 


# delete function 
def delete_data():
    data = {
        'id':1,
    }
    # convert dict into json 
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    try:
        data = r.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Response content is not valid JSON")
        print(r.text) 


# read
# get_data()

# post 
# post_data()


# update

# update_data()

# delete 
delete_data()




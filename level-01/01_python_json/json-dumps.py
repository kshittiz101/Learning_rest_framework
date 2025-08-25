# Convert python to json  (serializtions)
#  python provide json module to work with json
# to convert python data to json we use dumps method

import json
python_data = {
    'name': 'kshittiz',
    'age': 23,
    'isAdult': True,
    'address': {
        'country': 'Nepal',
        'province': '3',
        'city': 'kathmandu',
    }
}
# converting python data to json string
json_str = json.dumps(python_data)
print(json_str)
print(type(json_str))

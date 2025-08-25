# Convert JSON → Python (Deserialization)
# we can convert JSON data back to python data is process called Deserialization
# we can use json.loads methos to convert json data to python data


import json
json_data = '{"name": "kshittiz", "age": 23, "isAdult": true, "address": {"country": "Nepal", "province": "3", "city": "kathmandu"}, "job":"full stack developer"}'
parse_data = json.loads(json_data)
print(parse_data)
print(type(parse_data))

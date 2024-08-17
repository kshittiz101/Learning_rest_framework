# python has built in package called json, with is use to work with json data

# dumps(python_object) --> this method is used convert python object into json
# the process of converting pyhton object into json data called serialization
import json
python_data = {
    'name': 'kshittiz',
    'age': 22
}

# converting python dict into json
python_json = json.dumps(python_data)
print(type(python_json))
print(python_json)


# loads(json_data) --> this method is used to convert json string into python object
# the process of converting json string into python object is called deserialization

json_string = '{"name":"kshittiz" , "age": 22}'

python_dict = json.loads(json_string)
print(type(python_dict))
print(python_dict)

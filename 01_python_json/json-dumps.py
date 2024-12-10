# python json
# python json is module or package which is use to work with json data
# Important Methods in json module
# 1. dumps(data)
# this method is use to converts python objects into json string
import json
python_data = {'name':'kshittiz', 'address':'nepal'}
# converting python data to json string 
json_data = json.dumps(python_data)
print(json_data)
print(type(json_data))




# json loads() --> method is used to converts json data into python data
import json
json_data = '{"name":"kshittiz", "address":"Nepal"}'
parse_data = json.loads(json_data)
print(parse_data)
print(type(parse_data))

# Python json

In Python, JSON (JavaScript Object Notation) is a lightweight data format used for storing and exchanging data. It is easy for humans to read and write, and easy for machines to parse and generate. JSON is often used to send data between a server and a web application or between different parts of an application.

Python provides a built-in module called `json` to work with JSON data. This module allows you to:

- **Convert Python objects to JSON strings:** This process is known as serialization or encoding.
- **Convert JSON strings to Python objects:** This process is known as deserialization or decoding.

Here are some common operations you can perform with the `json` module:

### 1. Converting Python objects to JSON (Serialization)

```python
import json

# Python object (dictionary)
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": {
        "city": "New York",
        "zipcode": "10001"
    }
}

# Convert Python object to JSON string
json_string = json.dumps(data)
print(json_string)
```

### 2. Converting JSON strings to Python objects (Deserialization)

```python
import json

# JSON string
json_string = '{"name": "Alice", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": {"city": "New York", "zipcode": "10001"}}'

# Convert JSON string to Python object (dictionary)
data = json.loads(json_string)
print(data)
```

### 3. Reading and Writing JSON Files

You can also work with JSON data stored in files:

- **Writing JSON data to a file:**

  ```python
  import json

  data = {
      "name": "Alice",
      "age": 30,
      "is_student": False,
      "courses": ["Math", "Science"]
  }

  with open("data.json", "w") as file:
      json.dump(data, file)
  ```

- **Reading JSON data from a file:**

  ```python
  import json

  with open("data.json", "r") as file:
      data = json.load(file)
      print(data)
  ```

### Key Points:

- JSON uses a key-value pair format similar to Python dictionaries.
- JSON supports data types like strings, numbers, arrays (lists in Python), booleans, and objects (dictionaries in Python).
- In JSON, all keys must be strings, and strings are enclosed in double quotes.

The `json` module is very useful when you need to work with APIs, configuration files, or any other data interchange format that uses JSON.

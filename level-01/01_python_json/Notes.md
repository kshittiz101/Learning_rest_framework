# Python and JSON

## 1. What is JSON?

- **JSON** stands for _JavaScript Object Notation_.
- A **lightweight data-interchange format** (text-based).
- Easy to read and write for humans; easy to parse and generate for machines.
- Commonly used in **APIs, configuration, and data exchange**.

**JSON Data Types**:

- Object → `{ "key": "value" }`
- Array → `[1, 2, 3]`
- String → `"Hello"`
- Number → `42`, `3.14`
- Boolean → `true` / `false`
- Null → `null`

---

## 2. Python and JSON

Python provides the built-in **`json`** module to work with JSON data.

```python
import json
```

### a) Convert Python → JSON (Serialization)

```python
import json

data = {
    "name": "Krishna",
    "age": 23,
    "skills": ["Python", "Django", "Vue.js"]
}

# Convert dict to JSON string
json_string = json.dumps(data)

print(json_string)
# {"name": "Krishna", "age": 23, "skills": ["Python", "Django", "Vue.js"]}
```

### b) Convert JSON → Python (Deserialization)

```python
import json

json_string = '{"name": "Krishna", "age": 23, "skills": ["Python", "Django", "Vue.js"]}'

# Convert JSON string to dict
python_dict = json.loads(json_string)

print(python_dict["name"])  # Krishna
print(type(python_dict))    # <class 'dict'>
```

---

## 3. Working with JSON Files

### Write JSON to a file

```python
import json

data = {"project": "notes_project", "language": "Python"}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # indent makes it pretty
```

### Read JSON from a file

```python
import json

with open("data.json", "r") as f:
    content = json.load(f)

print(content["project"])  # notes_project
```

---

## 4. Options in `json` module

- `json.dumps(obj, indent=4)` → pretty print JSON.
- `json.dumps(obj, sort_keys=True)` → sort keys alphabetically.
- `json.loads(str)` → parse JSON string.
- `json.dump(obj, file)` → write JSON to file.
- `json.load(file)` → read JSON from file.

---

✅ **Summary**

- JSON is a universal format for data exchange.
- In Python, use the `json` module:

  - `dumps`/`loads` → string conversion.
  - `dump`/`load` → file operations.

# Deserialization

**Deserialization** is the process of converting data from a format that can be easily stored or transmitted (like JSON, XML, or a dictionary) back into a Python object (such as a model instance or a dictionary) that can be used in the application.

In Django REST Framework (DRF), deserialization specifically refers to converting JSON data from a request into a Python object and validating it using a serializer before saving it to the database.

### Example:

- **Serialized data**: A JSON object `{"name": "John", "age": 30}`.
- **Deserialized data**: Converting this JSON back into a Python dictionary or object, like `{"name": "John", "age": 30}` or an instance of the `Person` model.

Deserialization is essential for processing incoming data, ensuring it matches the required structure and validating it before further use.

## Documentation for De-serialization

Here’s a structured and clear documentation following the pattern of **Model**, **Serializer**, and **Views**, followed by a Python script for posting data:

---

## **1. Model**

### **Student Model**

This model represents a `Student` entity with fields for `name`, `roll number`, and `address`.

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)  # Stores the student's name
    roll = models.IntegerField()            # Stores the roll number
    address = models.CharField(max_length=100)  # Stores the student's address

    def __str__(self):
        return self.name  # Return the student's name when printing the object
```

### **Explanation**:

- **`name`**: A `CharField` to store the student's name (maximum length: 100).
- **`roll`**: An `IntegerField` to store the student's roll number.
- **`address`**: A `CharField` to store the student's address (maximum length: 100).
- **`__str__()`**: This method returns the student's name when the object is printed.

---

## **2. Serializer**

### **StudentSerializer**

The serializer is used to convert the `Student` model instances to JSON data and vice versa.

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'address']  # Specify the fields to be serialized
```

### **Explanation**:

- **`ModelSerializer`**: This is a DRF class that automatically generates a serializer based on the `Student` model.
- **`Meta` Class**: Specifies the model (`Student`) and the fields to include in the serialized data (`id`, `name`, `roll`, and `address`).

---

## **3. Views**

### **Student Create View**

This view handles the creation of a new student by accepting a `POST` request containing JSON data.

```python
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # Disables CSRF protection for this view (use cautiously)
def student_create(request):
    if request.method == 'POST':
        json_data = request.body  # Extract the raw JSON data from the request body
        try:
            # Convert the JSON data into a stream and parse it
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)

            # Deserialize the data using the serializer
            serializer = StudentSerializer(data=python_data)

            if serializer.is_valid():  # Check if the data is valid
                serializer.save()  # Save the valid data to the database
                response_data = {'msg': 'Data Created Successfully'}
                # Render the success message in JSON format
                json_response = JSONRenderer().render(response_data)
                return HttpResponse(json_response, content_type='application/json')

            # Return validation errors if the data is invalid
            json_response = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_response, content_type='application/json', status=400)

        except JSONParser.ParseError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    # If the method is not POST, return a "Method not allowed" error
    return JsonResponse({'error': 'Method not allowed'}, status=405)
```

### **Explanation**:

- **`@csrf_exempt`**: Disables CSRF validation for this view. While convenient for testing, it is **not recommended** for production. Use CSRF tokens for security in production.
- **`request.body`**: Extracts the raw JSON data from the request.
- **`JSONParser().parse()`**: Converts the raw JSON into Python data (a dictionary).
- **`StudentSerializer`**: Validates and deserializes the data into a `Student` object.
- **`serializer.is_valid()`**: Checks if the data passes validation.
- **`serializer.save()`**: Saves the valid data to the database.
- **Error Handling**: If there is an issue with the request data (invalid JSON or bad method), the view returns an appropriate error message.

---

## **4. Python Script to Post Data**

### **Posting Data Using Python `requests`**

Here’s a Python script that uses the `requests` library to send data to the `student_create` view.

```python
import requests
import json

# URL of the API endpoint where the student data will be posted
url = "http://localhost:8000/api/students/"  # Replace with the actual URL

# Data to be sent in the POST request (student data)
data = {
    'name': 'John Doe',
    'roll': 101,
    'address': '123 Main St'
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
```

### **Explanation**:

- **`url`**: Replace `"http://localhost:8000/api/students/"` with the actual URL of your API endpoint.
- **`data`**: A Python dictionary representing the student data to be sent in the request.
- **`json.dumps(data)`**: Converts the Python dictionary into a JSON-formatted string.
- **`headers`**: Specifies that the request body is in JSON format (`'Content-Type': 'application/json'`).
- **`requests.post()`**: Sends a POST request to the API with the provided data and headers.
- **`response.status_code`**: Checks the status code of the response.
- **`response.json()`**: Parses the JSON response from the server.

---

### **Expected Request and Response**

#### **Request (POST) Example**:

```json
{
  "name": "John Doe",
  "roll": 101,
  "address": "123 Main St"
}
```

#### **Response (Success)**:

```json
{
  "msg": "Data Created Successfully"
}
```

#### **Response (Validation Error)**:

```json
{
  "roll": ["This field must be unique."]
}
```

#### **Response (Invalid JSON)**:

```json
{
  "error": "Invalid JSON"
}
```

#### **Response (Method Not Allowed)**:

```json
{
  "error": "Method not allowed"
}
```

---

### **Recap of Steps**

1. **Model**: Define the `Student` model with fields for `name`, `roll`, and `address`.
2. **Serializer**: Use `ModelSerializer` to serialize and deserialize `Student` objects.
3. **View**: Create a view that handles the `POST` request to create a student.
4. **Post Data**: Use a Python script to send student data to the API.

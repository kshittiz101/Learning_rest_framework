Django REST Framework (DRF) crud project using ***Function Based Views(FBVs) api_view***, from creating the `Book` model to setting up views and URLs.

### 1. **Define the `Book` Model**

First, you need to define the `Book` model in your Django app's `models.py` file.

```python
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
```

### 2. **Create the `BookSerializer`**

Next, create a serializer to convert `Book` instances into JSON and vice versa. Add the following in a file called `serializers.py` within the same app.

```python
# serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

### 3. **Create the Views**

In your `views.py` file, you can now use the `BookSerializer` and `Book` model to create views that handle GET, POST, PUT, and DELETE requests.

```python
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def book_get_or_create(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        book.delete()
        return Response({'msg': 'Delete successfully'}, status=status.HTTP_204_NO_CONTENT)
```

### 4. **Set Up URLs**

Now, you need to create URLs to access these views. Modify your app's `urls.py` or create it if it doesn’t exist:

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_get_or_create, name='book-list-create'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
]
```

### 5. **Include App URLs in the Project's `urls.py`**

You need to include the app's URLs in the project's main `urls.py` file, usually located in the project root directory.

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_app_name.urls')),  # Include your app's URLs
]
```

### 6. **Run Migrations**

Before you can use the model, make sure to create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. **Testing the API with Postman**

You can now test your API using Postman:

- **GET** `/api/books/` - Retrieves a list of all books.
- **POST** `/api/books/` - Creates a new book.
- **GET** `/api/books/<id>/` - Retrieves a specific book by its ID.
- **PUT** `/api/books/<id>/` - Updates a specific book by its ID.
- **DELETE** `/api/books/<id>/` - Deletes a specific book by its ID.

### 8. **Admin Setup (Optional)**

To manage `Book` objects through the Django admin, register the model in the admin:

```python
# admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

This setup provides a fully functional API for managing `Book` resources.

## 2. Api Testing
Here’s the documentation for the provided Django REST Framework views (`book_get_or_create` and `book_detail`) that handle operations on the `Book` model.

---

## `book_get_or_create` View

### URL
- **Endpoint**: `/api/books/`
- **Methods Supported**: `GET`, `POST`

### Description
This view allows you to either retrieve a list of all books or create a new book in the database.

### Methods

#### `GET`
- **Description**: Retrieve a list of all `Book` objects stored in the database.
- **Response**:
  - **Status Code**: `200 OK`
  - **Content**: A JSON array of all books, with each book serialized as:
    ```json
    [
        {
            "id": 1,
            "title": "Book Title",
            "author": "Author Name",
            "published_date": "YYYY-MM-DD",
            "isbn": "ISBN Number"
        },
        ...
    ]
    ```

#### `POST`
- **Description**: Create a new `Book` object.
- **Request Body**:
  - **Content Type**: `application/json`
  - **Expected JSON Format**:
    ```json
    {
        "title": "Book Title",
        "author": "Author Name",
        "published_date": "YYYY-MM-DD",
        "isbn": "ISBN Number"
    }
    ```
- **Response**:
  - **Status Code**: `201 Created`
  - **Content**: The newly created `Book` object, serialized as:
    ```json
    {
        "id": 1,
        "title": "Book Title",
        "author": "Author Name",
        "published_date": "YYYY-MM-DD",
        "isbn": "ISBN Number"
    }
    ```
  - **Error Responses**:
    - **Status Code**: `400 Bad Request`
    - **Content**: A JSON object containing error messages, such as field validation errors.

### Example

- **Request**:
  ```http
  POST /api/books/
  Content-Type: application/json

  {
      "title": "The Hobbit",
      "author": "J.R.R. Tolkien",
      "published_date": "1937-09-21",
      "isbn": "9780261102217"
  }
  ```

- **Response**:
  ```http
  HTTP/1.1 201 Created
  Content-Type: application/json

  {
      "id": 1,
      "title": "The Hobbit",
      "author": "J.R.R. Tolkien",
      "published_date": "1937-09-21",
      "isbn": "9780261102217"
  }
  ```

---

## `book_detail` View

### URL
- **Endpoint**: `/api/books/<pk>/`
- **Methods Supported**: `GET`, `PUT`, `DELETE`

### Description
This view allows you to retrieve, update, or delete a specific `Book` object identified by its primary key (`pk`).

### Methods

#### `GET`
- **Description**: Retrieve the details of a specific `Book` object.
- **URL Parameter**:
  - **`pk`**: The primary key of the `Book` object to retrieve.
- **Response**:
  - **Status Code**: `200 OK`
  - **Content**: The `Book` object, serialized as:
    ```json
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "published_date": "1937-09-21",
        "isbn": "9780261102217"
    }
    ```
  - **Error Responses**:
    - **Status Code**: `404 Not Found`
    - **Content**: A JSON object indicating that the book was not found:
      ```json
      {
          "error": "Book not found"
      }
      ```

### Example

- **Request**:
  ```http
  GET /api/books/1/
  ```

- **Response**:
  ```http
  HTTP/1.1 200 OK
  Content-Type: application/json

  {
      "id": 1,
      "title": "The Hobbit",
      "author": "J.R.R. Tolkien",
      "published_date": "1937-09-21",
      "isbn": "9780261102217"
  }
  ```

#### `PUT`
- **Description**: Update the details of a specific `Book` object.
- **URL Parameter**:
  - **`pk`**: The primary key of the `Book` object to update.
- **Request Body**:
  - **Content Type**: `application/json`
  - **Expected JSON Format**:
    ```json
    {
        "title": "The Hobbit - Revised Edition",
        "author": "J.R.R. Tolkien",
        "published_date": "1951-09-21",
        "isbn": "9780261102217"
    }
    ```
- **Response**:
  - **Status Code**: `200 OK`
  - **Content**: The updated `Book` object, serialized as:
    ```json
    {
        "id": 1,
        "title": "The Hobbit - Revised Edition",
        "author": "J.R.R. Tolkien",
        "published_date": "1951-09-21",
        "isbn": "9780261102217"
    }
    ```
  - **Error Responses**:
    - **Status Code**: `400 Bad Request`
    - **Content**: A JSON object containing error messages, such as field validation errors.

### Example

- **Request**:
  ```http
  PUT /api/books/1/
  Content-Type: application/json

  {
      "title": "The Hobbit - Revised Edition",
      "author": "J.R.R. Tolkien",
      "published_date": "1951-09-21",
      "isbn": "9780261102217"
  }
  ```

- **Response**:
  ```http
  HTTP/1.1 200 OK
  Content-Type: application/json

  {
      "id": 1,
      "title": "The Hobbit - Revised Edition",
      "author": "J.R.R. Tolkien",
      "published_date": "1951-09-21",
      "isbn": "9780261102217"
  }
  ```

#### `DELETE`
- **Description**: Delete a specific `Book` object.
- **URL Parameter**:
  - **`pk`**: The primary key of the `Book` object to delete.
- **Response**:
  - **Status Code**: `204 No Content`
  - **Content**: A confirmation message indicating successful deletion:
    ```json
    {
        "msg": "Delete successfully"
    }
    ```
  - **Error Responses**:
    - **Status Code**: `404 Not Found`
    - **Content**: A JSON object indicating that the book was not found:
      ```json
      {
          "error": "Book not found"
      }
      ```

### Example

- **Request**:
  ```http
  DELETE /api/books/1/
  ```

- **Response**:
  ```http
  HTTP/1.1 204 No Content
  Content-Type: application/json

  {
      "msg": "Delete successfully"
  }
  ```

--- 

This documentation describes how to interact with the API endpoints provided by the `book_get_or_create` and `book_detail` views, including the expected request formats and possible responses.
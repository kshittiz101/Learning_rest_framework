# Class Based View (api)

Django Rest Framework (DRF) offers a variety of Class-Based Views (CBVs) that simplify the process of building RESTful APIs. These views provide different levels of abstraction and flexibility, allowing you to handle common API patterns efficiently. Here are the different types of CBVs in DRF:

### 1. **APIView**

- **Basic Overview:** `APIView` is the most fundamental class-based view in DRF. It provides the foundation for building your API views but doesn’t impose any specific behavior or response format. You can customize the `get`, `post`, `put`, `delete`, etc., methods to handle HTTP requests.
- **Example:**

  ```python
  from rest_framework.views import APIView
  from rest_framework.response import Response

  class MyAPIView(APIView):
      def get(self, request, format=None):
          data = {"message": "GET request"}
          return Response(data)

      def post(self, request, format=None):
          data = {"message": "POST request"}
          return Response(data)
  ```

### 2. **Generic Views**

- **Basic Overview:** DRF’s generic views offer a more abstracted way to build views. These views handle common patterns such as displaying a list of objects, retrieving a specific object, creating, updating, or deleting objects.
- **Common Generic Views:**

  - **ListAPIView:** Handles listing objects.
  - **CreateAPIView:** Handles creating new objects.
  - **RetrieveAPIView:** Handles retrieving a specific object.
  - **UpdateAPIView:** Handles updating an existing object.
  - **DestroyAPIView:** Handles deleting an object.

- **Example:**

  ```python
  from rest_framework.generics import ListAPIView
  from .models import MyModel
  from .serializers import MyModelSerializer

  class MyModelListView(ListAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

### 3. **Mixins**

- **Basic Overview:** DRF provides mixins that encapsulate common behaviors (like create, retrieve, update, and destroy) which you can combine to create your own custom views.
- **Common Mixins:**
  - `CreateModelMixin`: Adds create behavior to a view.
  - `RetrieveModelMixin`: Adds retrieve behavior to a view.
  - `UpdateModelMixin`: Adds update behavior to a view.
  - `DestroyModelMixin`: Adds destroy behavior to a view.
  - `ListModelMixin`: Adds list behavior to a view.
- **Example:**

  ```python
  from rest_framework import generics, mixins
  from .models import MyModel
  from .serializers import MyModelSerializer

  class MyModelView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer

      def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)

      def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)
  ```

### 4. **ViewSets**

- **Basic Overview:** ViewSets allow you to combine the logic for handling multiple actions (like listing, retrieving, creating, updating, and deleting) into a single class. This approach is particularly useful when creating RESTful APIs that adhere to standard URL patterns.
- **Types of ViewSets:**
  - **ModelViewSet:** Combines list, create, retrieve, update, and destroy actions.
  - **ReadOnlyModelViewSet:** Combines list and retrieve actions only.
- **Example:**

  ```python
  from rest_framework import viewsets
  from .models import MyModel
  from .serializers import MyModelSerializer

  class MyModelViewSet(viewsets.ModelViewSet):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

  - **Routing ViewSets:** You typically use DRF’s router to automatically generate URL patterns for ViewSets.

    ```python
    from rest_framework.routers import DefaultRouter
    from .views import MyModelViewSet

    router = DefaultRouter()
    router.register(r'mymodels', MyModelViewSet)

    urlpatterns = router.urls
    ```

### 5. **Custom ViewSets**

- **Basic Overview:** You can customize the actions and behaviors of a `ViewSet` by overriding methods or defining custom actions. This approach gives you full control over the request handling process.
- **Example:**

  ```python
  from rest_framework import viewsets
  from rest_framework.decorators import action
  from rest_framework.response import Response
  from .models import MyModel
  from .serializers import MyModelSerializer

  class MyModelViewSet(viewsets.ModelViewSet):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer

      @action(detail=True, methods=['get'])
      def custom_action(self, request, pk=None):
          instance = self.get_object()
          return Response({'custom': instance.custom_field})
  ```

### 6. **Customizing Views with Mixins and Generics**

- Sometimes you need a custom view that doesn’t fit neatly into the standard DRF views. In such cases, you can mix and match generic views with mixins to create highly customized views.
- **Example:**

  ```python
  from rest_framework import mixins, generics

  class CustomAPIView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer

      def perform_create(self, serializer):
          # Custom logic during create
          serializer.save(owner=self.request.user)
  ```

### 7. **Hybrid Approaches**

- You can combine function-based views with class-based views to handle specific cases where you need a simpler or more complex approach than what DRF’s CBVs offer.

### Conclusion

DRF’s Class-Based Views (CBVs) offer a powerful and flexible way to handle HTTP requests in a RESTful API. Whether you need simple or highly customized views, DRF provides the tools to help you build robust APIs efficiently.

# APIView

## **What is ApiView ?**

`APIView` is a class provided by Django REST Framework (DRF) that allows you to create custom API views in Django. It provides a base for building more complex, fully customizable views by handling common tasks like request parsing, response rendering, and exception handling.

Unlike DRF's generic views or viewsets, `APIView` gives you complete control over the request-response cycle. You manually define methods like `get`, `post`, `put`, `patch`, and `delete` to handle different HTTP methods, making it ideal for scenarios where you need fine-grained control over the logic of your API.

## When To use APIView ?

You should use `APIView` in Django REST Framework in the following scenarios:

### 1. **Fine-Grained Control**:

- **Custom Logic**: When you need complete control over the request-response cycle and need to implement custom logic that doesn't fit well with the more abstracted generic views or viewsets.
- **Custom Request/Response Handling**: When you need to customize how requests are parsed or how responses are rendered. For example, if you need to support a non-standard response format or handle authentication in a unique way.

### 2. **Non-Standard HTTP Methods**:

- If your API needs to handle HTTP methods that aren't covered by the typical CRUD operations (GET, POST, PUT, DELETE), such as PATCH or OPTIONS, `APIView` allows you to define these methods manually.

### 3. **Simple APIs Without CRUD**:

- **Basic API Endpoints**: When you need a simple API endpoint that doesn’t map directly to CRUD operations on a model, such as a status check or an endpoint that performs an action (like sending an email) without directly interacting with a database model.

### 4. **Performance Optimization**:

- If you want to avoid some of the overhead associated with DRF’s more abstracted views (like the generic views or viewsets), `APIView` allows you to implement just the functionality you need, which can lead to performance improvements.

### 5. **Learning Purposes**:

- For educational purposes, using `APIView` can help you understand the underlying mechanisms of Django REST Framework by making you implement parts of the process manually, which can be hidden by generic views or viewsets.

### 6. **When You Don’t Need Full CRUD**:

- If your view only needs to handle a subset of CRUD operations (for example, just GET and POST), using `APIView` allows you to define only the methods you need without the overhead of unused functionality.

### 7. **Custom Error Handling**:

- If you need specific error handling behavior that isn’t easily managed by generic views, `APIView` lets you define custom responses for different exceptions.

### Example Use Cases:

- **Authentication Endpoints**: Custom login, logout, or token handling.
- **Webhooks**: Handling incoming requests from external services where the request may need to be processed differently than standard CRUD operations.
- **Complex Querying**: When the data retrieval logic is complex and doesn’t map neatly to a queryset.

## How to Use ?

To use `APIView` in Django REST Framework (DRF), follow these steps:

### 1. **Install Django REST Framework**

First, make sure you have Django REST Framework installed in your Django project.

```bash
pip install djangorestframework
```

Add `'rest_framework'` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # other apps
    'rest_framework',
]
```

### 2. **Create a Django App**

If you don’t already have an app where you want to create the API view, you can create one using:

```bash
python manage.py startapp myapp
```

### 3. **Define a Model (Optional)**

If your API will interact with a database model, define the model in `models.py`. For example:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
```

Run migrations to create the database table:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. **Create a Serializer (Optional)**

If you're dealing with a model, you'll typically create a serializer to convert model instances to JSON and vice versa. Define it in `serializers.py`:

```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

### 5. **Create the API View**

Now, you can create your API view using `APIView`. Define it in `views.py`:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404

class BookListCreateAPIView(APIView):
    """
    Handles GET and POST requests for the Book model.
    """
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailAPIView(APIView):
    """
    Handles GET, PUT, DELETE requests for a single Book instance.
    """
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

```

### 6. **Define the URLs**

You need to map the views to URLs. Do this in `urls.py`:

```python
from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
]

```

### 7. **Run the Django Development Server**

Start your Django server to test the API.

```bash
python manage.py runserver
```

### 8. **Test the API**

You can now test your API using tools like Postman, curl, or even your browser (for GET requests).

- **GET /books/**: Returns a list of all books.
- **POST /books/**: Creates a new book.
- **GET /books/{id}/**: Retrieves a specific book by its ID.
- **PUT /books/{id}/**: Updates a specific book by its ID.
- **DELETE /books/{id}/**: Deletes a specific book by its ID.

### Summary

- `APIView` is used for creating API endpoints where you have full control over the request and response cycle.
- You can define methods like `get`, `post`, `put`, and `delete` to handle the respective HTTP methods.
- This approach is ideal when you need custom logic or when the built-in generic views don't fit your needs.

This is how you use `APIView` in Django REST Framework to create fully customizable API endpoints.



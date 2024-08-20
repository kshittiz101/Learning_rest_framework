from rest_framework import serializers
from .models import Student

# normal serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    email = serializers.EmailField()

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    def update(self,instance, validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.age = validate_data.get('age',instance.age)
        instance.email = validate_data.get('email',instance.email)
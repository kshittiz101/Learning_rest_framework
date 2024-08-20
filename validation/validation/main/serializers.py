from rest_framework import serializers
from .models import Student
import re


def valid_email_pattern(value):
    pattern = r'^[a-zA-Z0-9._%+-]+@example\.com$'
    if not re.match(pattern,value):
        raise serializers.ValidationError("invalid email pattern")
    return value
    
# normal serializers
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    # using validators
    email = serializers.EmailField(validators =[valid_email_pattern])

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    # update 
    def update(self,instance, validate_data):
        # old data
        print(instance.name)
        instance.name= validate_data.get('name',instance.name)
        # new data
        print(instance.name)
        instance.age= validate_data.get('age',instance.age)
        instance.email= validate_data.get('email',instance.email)
        instance.save()
        return instance
    
    # validation 
    # Field validation (single field validation)
    def validate_age(self,value):
        if value <= 0: 
            raise serializers.ValidationError('age must be greater than 0')
        return value
    
    # object level validation
    # def validate(self,data):
    #     name = data.get('name')
    #     age = data.get('age')
    #     email = data.get('email')

    #     # if not name:
    #     #     raise serializers.ValidationError("Name field can't be empty")
        
    #     # if not email:
    #     #     raise serializers.ValidationError("Email field can't be empty")

    #     if email[0] != email[0].lower():
    #         raise serializers.ValidationError('The first letter of email always be lowercase')
    #     return data
    



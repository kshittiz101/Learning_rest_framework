from rest_framework import serializers
from .models import Book
class BookSerializer(serializers.ModelSerializer):
    is_published = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ('title','is_published')
    
    def get_is_published(self,obj):
        return obj.title
        
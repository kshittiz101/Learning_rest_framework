from django.contrib import admin
from api.models import Books


# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'author']

from django.contrib import admin
from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    search_fields = ['title']


# register bookadmin
admin.site.register(Book, BookAdmin)

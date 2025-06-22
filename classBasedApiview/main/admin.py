from django.contrib import admin
from .models import Books


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date', 'isbn', 'price')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('published_date',)

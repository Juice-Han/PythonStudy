from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Book, BookAdmin)

from django.urls import path
from .views import HelloAPI, bookAPI, booksAPI, BookAPI, BooksAPI

urlpatterns = [
    path('hello/', HelloAPI),
    path('fbv/book/', booksAPI),
    path('fbv/book/<int:bid>/', bookAPI),
    path('cbv/book/', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view()),
]
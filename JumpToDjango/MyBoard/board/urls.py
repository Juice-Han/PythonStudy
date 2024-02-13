from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:book_id>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
]

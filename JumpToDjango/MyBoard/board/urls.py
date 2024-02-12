from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('posts/', views.posts, name='posts'),
    path('write/', views.write, name='write'),
]

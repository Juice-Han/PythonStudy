from django.db import models
from django.utils import timezone

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    book_image = models.ImageField(upload_to='images/', null=True)
    create_dt = models.DateTimeField()
    modify_dt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

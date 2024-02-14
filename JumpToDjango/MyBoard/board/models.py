import os

from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    book_image = models.ImageField(upload_to='images/', null=True)
    create_dt = models.DateTimeField()
    modify_dt = models.DateTimeField(null=True, blank=True)

    def delete(self, *args, **kargs):
        if self.book_image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.book_image.path))
        super(Book, self).delete(*args, **kargs)

    def __str__(self):
        return self.title

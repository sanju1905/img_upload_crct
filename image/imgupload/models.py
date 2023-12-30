# gallery/models.py
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

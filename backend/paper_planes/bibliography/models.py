from django.db import models

# Create your models here.

class Paper(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    journal = models.CharField(max_length=50)
    pages = models.CharField(max_length=25)
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.title


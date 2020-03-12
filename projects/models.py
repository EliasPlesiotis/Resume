from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    link = models.CharField(max_length=100)
    code = models.CharField(max_length=200)
    image = models.FileField()
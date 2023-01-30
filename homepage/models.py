from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=5000)
    image = models.ImageField()
    description = models.CharField(max_length=100000)
    url = models.CharField(max_length=500)
from django.db import models

# Create your models here.
class signup(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact_number=models.IntegerField()
    college_name=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    course_year=models.CharField(max_length=150)
    instagram_url=models.CharField(max_length=500)
    twitter_url=models.CharField(max_length=500)
    facebook_url=models.CharField(max_length=500)
    confirmation = models.CharField(max_length=10)

    def __str__(self):
        return self.username
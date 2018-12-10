from django.db import models

# Create your models here.
class userinfo(models.Model):
    username=models.CharField(max_length=64)
    gender=models.CharField(max_length=64)
    age=models.CharField(max_length=64)


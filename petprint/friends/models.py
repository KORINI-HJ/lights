from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class follow(models.Model):
    followee = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
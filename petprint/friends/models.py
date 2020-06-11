from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee')

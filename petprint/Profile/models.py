from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    pet_name = models.CharField(max_length=20,null=True)
    pet_image = models.ImageField(null=True, upload_to='profile')
    pet_explain = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.pet_name

class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lover')
    followee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lovee')

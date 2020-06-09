from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=100)
    #user = models.CharField(default=settings.AUTH_USER_MODEL)
    body = models.TextField()
    images = models.ImageField(default='default.jpg', upload_to='%Y/%m/%d/%H/%m')
    time = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    #emotion = models.Choices

    def __str__(self):
        return self.title
'''
# User 유저
class User(models.Model):
    password = models.CharField(max_length=20)
'''
# 댓글
class Comment(models.Model):
    post = models.ForeignKey(Diary, on_delete=models.CASCADE)
    body = models.CharField('comment', max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

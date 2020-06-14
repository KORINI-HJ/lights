from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
 
# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=100)
    #user = models.CharField(default=settings.AUTH_USER_MODEL)
    body = RichTextUploadingField()
    images = models.ImageField(default='null', upload_to='%Y/%m/%d/%H/%m')
    time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    #emotion = models.Choices

    def __str__(self):
        return self.title

# 댓글
class Comment(models.Model):
    post = models.ForeignKey(Diary, on_delete=models.CASCADE)
    body = models.CharField('comment', max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
'''
class HashTag(models.Model):
    tag = models.CharField(max_length=20, unique=True)
    diary = models.ManyToManyField(Diary)

    def __str__(self):
        return self.tag

'''
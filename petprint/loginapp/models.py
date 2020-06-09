from django.db import models
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

@receiver(post_save, sender=User)
def create_user_nickname(sender, instance, created, **kwargs):
    if created:
        NickName.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_nickname(sender, instance, **kwargs):
    #instance.nickname.save()
    pass



class NickName(models.Model):
   
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('이름', max_length=5)
   
    def __str__(self):
        return self.nickname

from django.utils import timezone
# Create your models here.

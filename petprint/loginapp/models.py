from django.db import models
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Profile(models.Model):
    M_or_F = (
    ('남', '남'),
    ('여', '여'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField('이름', max_length=5)
    major = models.CharField('학과', max_length=30)
    phone_number = models.CharField('전화번호', max_length=20)
    m_or_f = models.CharField('성별', choices=M_or_F, max_length=2)
    email = models.EmailField('이메일', max_length=254)

    def __str__(self):
        return self.name

from django.utils import timezone
# Create your models here.

from django.contrib.auth.models import AbstractUser, User
from django.db import models

from monuments.models import Monument


# Create your models here.


# class User(AbstractUser):
#     first_name = models.CharField(max_length=50, blank=True, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=50, blank=True, null=True)
#     is_active = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.first_name + " " + self.last_name


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    monument = models.ForeignKey(Monument, related_name='favorites', on_delete=models.CASCADE)


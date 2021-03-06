from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, models.Model):
    name = models.CharField(max_length=100)

    profile_pic = models.URLField(default='')


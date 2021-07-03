from django.contrib.auth.models import User

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Profile(models.Model):
    #Profile models

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to = 'users/pictures', blank=True, null=True)

    create = models.DateTimeField(auto_now_add=True)
    modifie =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
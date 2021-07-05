#Posts models
# Django
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now= True)

    def __str__(self):
        return '{} by@{}'.format(self.title, self.user.username)
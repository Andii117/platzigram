#Posts form 

from django import forms
from django.db import models
from django.db.models import fields

#Model
from posts.models import Post

class PostForm(forms.ModelForm):
    #Post models forms

    class Meta:
        #Forms settings
        model = Post
        fields=('user','profile','title','photo')
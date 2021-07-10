from django.contrib import admin

#Models
from posts.models import Post

# Register your models here.

#Se registra en la consola de admin de python el modelo
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'photo', )

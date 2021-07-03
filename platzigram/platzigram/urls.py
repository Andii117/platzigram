
from django.contrib import admin
from django.urls import path
from platzigram import views as local_views
from posts import views as posts_views 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-word/', local_views.hello_word ),
    path('sorted/', local_views.hi ),
    path('hi/<str:name>/<int:age>', local_views.say_hi),
    path('posts/', posts_views.list_posts)
]

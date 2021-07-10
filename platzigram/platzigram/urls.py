
from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from platzigram import views as local_views
from posts import views as posts_views 
from users import views as users_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-word/', local_views.hello_word , name='hello_word'),
    path('sorted/', local_views.hi, name='sort' ),
    path('hi/<str:name>/<int:age>', local_views.say_hi, name='hi'),
    

    #path for Users
    path('users/login/', users_views.login_view ,name='login'),
    path('users/logout/',users_views.logout_view ,name='logout'),
    path('users/signup/',users_views.singup_view ,name='signup'),
    path('users/me/profile/',users_views.update_profile ,name='update_profile'),
    
    #path for Posts
    path('', posts_views.list_posts, name='feed'),
    path('posts/news/', posts_views.create_post, name='create_post'),
]# + static(settings.MEDIA_URL, document.root = settings.MEDIA_ROOT)

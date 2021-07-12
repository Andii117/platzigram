#Django
from django.urls import path
#Posts
from posts import views 


urlpatterns = [
#path for Posts
    path(
        route='',
        view=views.list_posts,
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.create_post,
        name='create_post'
    ),
]
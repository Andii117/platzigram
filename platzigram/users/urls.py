#Django
from django.urls import path
from django.views.generic import TemplateView
#Posts
from users import views 

urlpatterns = [

    #Posts
    #path(
    #    route='profile:<str:username>/',
    #    view= TemplateView.as_view(templatename='users/detail.html'),
    #    name='detail'
    #),

    #Managent
    #path for Users
    path(
        route='login/', 
        view =views.login_view ,
        name ='login'),
    path(
        route ='logout/',
        view  = views.logout_view ,
        name  ='logout'),
    path(
        route ='signup/',
        view  =views.singup_view ,
        name  ='signup'),
    path(
        route ='me/profile/',
        view  = views.update_profile ,
        name  ='update_profile'),
]
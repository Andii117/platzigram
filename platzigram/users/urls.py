#Django
from django.urls import path
#Posts
from users import views 

urlpatterns = [

    #Managent
    #path for Users
    path(
        route='login/', 
        view =views.LoginView.as_view() ,
        name ='login'),
    path(
        route ='logout/',
        view  = views.LogoutView.as_view() ,
        name  ='logout'),
    path(
        route ='signup/',
        view  =views.SignupView.as_view(),
        name  ='signup'),
    path(
        route ='me/profile/',
        view  = views.UpdateProfileView.as_view() ,
        name  ='update_profile'),


    #Posts
    #Siempre colocar los paths dinamicos de ultimas 
    #para que no cause un Bug encontrando las demas 
    #rutas
    path(
        route='<str:username>/',
        view= views.UserDetailView.as_view(),
        name='detail'
    ),
]
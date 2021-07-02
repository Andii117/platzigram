
from django.contrib import admin
from django.urls import path
from platzigram import views



urlpatterns = [
    path('hello-word/', views.hello_word ),
    path('sorted/', views.hi ),
    path('hi/<str:name>/<int:age>', views.say_hi)
]

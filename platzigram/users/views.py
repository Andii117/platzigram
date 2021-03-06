# Django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from django.views.generic import DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
# Models
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from posts.models import Post
from users.models import Profile

#Forms
from users.forms import SignupForm


#Lo que va encerrado dentro del parencesis es la forma de extender clases
class UserDetailView(LoginRequiredMixin,  DetailView):
    #User detail view

    template_name='users/detail.html'
    #Campo único(PK) del set de datos
    slug_field = 'username'
    #Nombre del lado de las urls (ejemplo: <str:username>/ el mismo que esta en las url's de user)
    slug_url_kwarg = 'username'
    #QuerySet  a partir de que conjunto de datos va a traer los datos 
    queryset = User.objects.all();
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        #Add User's potst to context
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class UpdateProfileView(LoginRequiredMixin,UpdateView):
    #Update profile view
    template_name ='users/update_profile.html'
    model = Profile
    fields= ['website', 'biography','phone_number','picture']

    def get_object(self):
        #Return user's profile
        return self.request.user.profile

    def get_success_url(self):
        #Return to user's profile
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    #Login view
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    #Logout view
    template_name = 'users/logged_out.html'



class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)




        
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from django.views.generic import DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
# Models
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from posts.models import Post
from users.models import Profile

#Forms
from users.forms import SignupForm

# Forms
from users.forms import ProfileForm

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




#Controlador vista login
def login_view(request):
    #Login view
    if request.method == 'POST':
        #Obtiene el username y password del login
        username = request.POST['username']
        password = request.POST['password']
        #Función para obtener el login autenticado
        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            #este es el name de la ruta en el arhivo urls.py  
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'invalid username and password'})
    #Renderea la pagina login.html de la carpeta templates
    return render(request, 'users/login.html')

#Controlador vista logout
@login_required
def logout_view(request):
    #logout a user
    logout(request)
    return redirect('users:login')



class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)




        
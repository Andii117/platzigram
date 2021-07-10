# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )



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
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'invalid username and password'})
    #Renderea la pagina login.html de la carpeta templates
    return render(request, 'users/login.html')

#Controlador vista logout
@login_required
def logout_view(request):
    #logout a user
    logout(request)
    return redirect('login')

#Controlador vista sing up
def singup_view(request):
    #Signup a user
    if request.method == 'POST':
        #Obtiene el username, password y password confirma
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirmation']
        #Valida que la contraseña y su confirmación coincidan
        if password != password_confirm: 
            #Si no coinciden muestra el error en la pantalla de signup
            return render(request, 'users/signup.html', {'error': 'password confirmation does not match'})
        #Intenta crear el usuario de la BD
        try:
            #Usuario guardado en DB
            user =  User.objects.create_user(username= username, password= password)
        #Si el usuario ya esta creado
        except IntegrityError:
            #Si el usuario a crear ya se encuentra registrado en la DB muestra el mensaje de error
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        #Obtiene los datos de first name last name y email del formulario
        user.first_name = request.POST['first_name'] 
        user.last_name  = request.POST['last_name'] 
        user.email      = request.POST['email'] 
        #Guarda la información del usuario
        user.save()

        #se crea el profile 
        profile = Profile(user=user)
        #Guarda la información del perfil
        profile.save()
        #Renderea al login
        return redirect('login')

    #renderea la pagina signup de la carpeta templates
    return render(request, 'users/signup.html')



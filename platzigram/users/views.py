# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Forms
from users.forms import ProfileForm, SignupForm

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
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(
        request=request,
        template_name='users/signup.html',
        context={
            'form' : form
        }
    )


        
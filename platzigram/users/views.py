from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Create your views here.

def login_view(request):
    #Login view
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user :
            login(request, user)
            #este es el name de la ruta en el arhivo urls.py  
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'invalid username and password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    #logout a user
    logout(request)
    return redirect('login')
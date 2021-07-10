#Django
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#Utilities
from datetime import datetime
#Forms
from posts.forms import PostForm
from posts.models import Post

#Data de ejemplo para valdiar el html del feed
"""
posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]
"""

# Create your views here.
@login_required
def list_posts(request):
    #Obtiene con consulta ORM los Post ordenados por fecha de creación en orden descendete
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html',{'posts': posts})

@login_required
def create_post(request):
    #Create new posts view
    if request.method == 'POST':
        #Obtiene la información del formulario y los archivo dentro de el
        #request.POST( Info formulario) request.FILES(Info archivo (foto))
        form = PostForm(request.POST, request.FILES)
        #valida el formulario
        if form.is_valid():
            #Guarda la información del formulario si es valido
            form.save()
            #Retorna la vista feed
            return redirect('feed')
    else:
        #Si es un formulario vacio
        form= PostForm()
    #Al final devuelve la vista news.html
    return render(
        request,
        template_name='posts/news.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
    
    

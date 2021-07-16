#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,DetailView
from django.urls import reverse_lazy

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
class PostsFeedView(LoginRequiredMixin, ListView):
    #Return all published posts

    #Ubicación del template a usar
    template_name = 'posts/feed.html'
    #Se usa el modelo de Post
    model = Post
    #Ordenamiento por creación desendientemente
    ordering = ('-created',)
    #Página la vista de posts a 30 
    paginate_by = 30
    #Se nombra el contexto a posts
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    #Return post detail

    #Template al cual se va a redirigie la petición
    template_name = 'posts/detail.html'
    #Queryset de donde obtiene la información
    queryset = Post.objects.all()
    #Contexto para mostrar los datos
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    #Create a new posts

    #Template al cual se va a redirigie la petición
    template_name = 'posts/new.html'
    #Queryset de donde obtiene la información
    form_class  = PostForm
    #El reverse_lazy es para mostrar la pagína pero únicamente cuando lo encesite
    success_url = reverse_lazy('posts:feed')
    
    #Contexto (sobrecarga de métodos)
    def get_context_data(self, **kwargs) :
        #Add user and profile context
        #Obtiene el contexto de la página
        context =  super().get_context_data(**kwargs)
        #Adiciona al contexto el usuario 
        context['user'] = self.request.user
        #Adiciona al contexto el profile
        context['profile'] = self.request.user.profile
        return context
    
    


from os import name
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

from users import views as users_views




urlpatterns = [
    path('admin/', admin.site.urls),
    #Cuando se trasladan las URL's para sus debidas carpetas
    #Se utiliza el includ, esta función dicta que
    #primero se define la carpeta donde se guardan las URL's
    #y despues el nombre de la aplicación, despues se da un 
    #namespace que es en el cual la URL's van a comenzar
    #por este motivo las rutas en los otros archivos
    #no comienzan por el nombre del proyecto.
    path('', include(('posts.urls','posts'),namespace='posts')),

    path('users/',include(('users.urls','users'), namespace='users')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

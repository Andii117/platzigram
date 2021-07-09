#Platzigram middlerware catalogo


# Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    #Profile completion middleware

    #Ensure every user that is interaction with the pltaform 
    #have their profile picture and biography.

    def __init__(self, get_response):
        #Middleware initialization 
        self.get_response = get_response

    def __call__(self, request):
        #Code to be executed for each request before the view is called.
        #Si no existe un usuario login
        if not request.user.is_anonymous:
            #Si no es usuario staff, esto sirve para que cuando entra como admin no se cargue la 
            #página de update_profile
            if not request.user.is_staff:
            #Obtiene el profile del user
                profile = request.user.profile
                #Si el profile no tiene el picture 
                if not profile.picture or not profile.biography:
                    #Validamos que el request no tiene la pagína que se desea cargar
                    #importamos la función de reverse que obtiene una url a partir del name
                    if request.path not in  [reverse('update_profile'),reverse('logout')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response


#Users forms

#Django
from django import forms
#Models
from django.contrib.auth.models import User
from users.models import Profile

class ProfileForm(forms.Form):
    #Profile forms

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()

class  SignupForm(forms.Form):
    #Sign up form

    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name  = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(min_length= 6 , max_length= 70, widget= forms.EmailInput)


    
    def clean_username(self):
        #Username must be unique.

        #Obtenemos el dato de username validado
        username = self.cleaned_data['username']
        #consultamos a bd si existe
        #filtre los usuarios en BD con username = username y obtenga todos los datos
        username_taken = User.objects.filter(username = username).exists()
        #Si existe el usuario         
        if username_taken :
            #Django se encarga de lanzar el error
            raise forms.ValidationError('Username  is already in use.')
        #En caso de que no este en uso, retorna el username
        return username

    def save(self):
        #Create user and profile

        #Obtenemos la información del formulario
        data = self.cleaned_data
        #Se saca de la lista el dato password_confirmation
        data.pop('password_confirmation')

        #import pdb; pdb.set_trace()
        #Se crea el usuario en BD
        user = User.objects.create_user(**data)
        #Se crea el profile en BD
        profile = Profile(user=user)
        #Se guarda en BD
        profile.save()



    def clean(self):
        #Verify password confirmation match.

        #Obtenemos la información
        data = super().clean()

        #Obtenemos el password
        password = data['password']
        #Obtenemos el password confirmation
        password_confirmation = data['password_confirmation']
        #Validamos que sean iguales
        if password != password_confirmation:
            raise forms.ValidationError('Password do not match.')
        
        return data
             

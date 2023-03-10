from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from .forms import UserForm
from django.contrib import messages
#    super(ModelName, self).save(*args, **kwargs) # Call the real save() method
from gestion_user.forms import UserRegisterForm, reserveForm
from gestion_admin.forms import GestionagenceCreate
from gestion_admin.models import Gestionagence

# import view sets from the REST framework
from rest_framework import viewsets
# import the userSerializer from the serializer file
from .serializers import userSerializer
# import the user model from the models file
from .models import UserRegisterform

# create a class for the user model viewsets
class userView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the userSerializer class
    serializer_class = userSerializer
 
    # define a variable and populate it
    # with the user objects
    queryset = UserRegisterform.objects.all()


def home(request):
    return render(request, 'home.html')

@login_required
def login(request):
    if request.method == 'POST':
        # form = UserLoginForm()
        email = request.POST['email']
        print('le mail est :',email)
        password = request.POST['password1']
        user = authenticate(request, email = email, password = password)
        if user is None and user.is_active:
            login(request, user)
            messages.success(request, 'connexion reussie')
            return redirect('home')
        else:
            messages.error(request, "Erreur d'authentification")
    return render(request, 'login.html')

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "compte cree avec succes ")
            return redirect('login')
        else:
            messages.error(request, form.errors)
    return render(request, 'register.html', {'form': form})

def disconnect(request):
    pass

def reservations(request):
    Forms = reserveForm()
    return render(request, 'reservations.html', {'Forms': Forms})

# def liste(request):
#     return render(request,'reservation_liste.html')

def visiter(request):
    return render(request, 'visiter.html')

def propos(request):
    return render(request, 'a_propos.html')

def home(request):
      shelf = Gestionagence.objects.all()
      return render(request, 'home.html', {'shelf': shelf})
def upload(request):
    upload = GestionagenceCreate()
    if request.method == 'POST':
        upload = GestionagenceCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save() 
            return redirect('home')
        else:
            return HTTPResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url:'home'}}">Reload</a> """)
    else:
        return render (request, 'upload_form.html', {'upload_form': upload})
    
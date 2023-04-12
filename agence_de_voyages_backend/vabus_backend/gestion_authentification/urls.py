from django.urls import path
from gestion_authentification.views import *
from gestion_authentification import views

urlpatterns = [
    path('login',views.LoginView.as_view(), name='login'),   
    path('register',views.RegistrationView.as_view(), name='register'),      
]
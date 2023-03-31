from django.urls import path
from gestion_authentification.views import *
from gestion_authentification import views

urlpatterns = [
     path('api/exemple/', views.example_view),
]
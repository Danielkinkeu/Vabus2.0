from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib import messages
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from gestion_reservation.forms import *
from .models import *
from django.contrib.auth.models import User

# import view sets from the REST framework
from rest_framework import viewsets
# import the userSerializer from the serializer file
from .serializers import reservationSerializer
from rest_framework.decorators import api_view
# import the user model from the models file
from .models import ReservationCreate

# create a class for the user model viewsets
class reservationView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the userSerializer class
    serializer_class = reservationSerializer
 
    # define a variable and populate it
    # with the user objects
    queryset = ReservationCreate.objects.all()


class ListReservationView(ListAPIView):
    queryset= ReservationCreate.objects.all()
    serializer_class= reservationSerializer

class CreateReservationView(CreateAPIView):
    queryset= ReservationCreate.objects.all()
    serializer_class= reservationSerializer
    
class UpdateReservationView(UpdateAPIView): 
    queryset= ReservationCreate.objects.all()
    serializer_class= reservationSerializer

class DeleteReservationView(DestroyAPIView):
    queryset= ReservationCreate.objects.all()
    serializer_class= reservationSerializer
 
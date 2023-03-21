from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib import messages
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


# Create your views here.
def reserver_form(request):
    upload = ReservationForm()
    user=request.user
    if request.method == 'POST':
        upload = ReservationForm(request.POST)
        reservationcreate=ReservationCreate()
        if upload.is_valid():
            reservationcreate.destination = upload.cleaned_data['destination']
            reservationcreate.depart = upload.cleaned_data['depart']
            reservationcreate.datedepart = upload.cleaned_data['datedepart']
            reservationcreate.qte = upload.cleaned_data['qte']
            reservationcreate.user = user
            reservationcreate.save()
            print(ReservationCreate.depart)
            reservations=ReservationCreate.objects.filter(user=user)
            return render(request, 'reservation_list.html',{'reservations':reservations})
        else:
            return render(request, 'reserver.html',{'upload':upload})
    else:
        return render (request, 'reserver.html', {'upload': upload})
    

def liste(request):
    user=request.user
    if user.username == 'vabus':
        reservations=ReservationCreate.objects.all()
    else:    
        reservations=ReservationCreate.objects.filter(user=user)
    return render(request, 'reservation_list.html', {'reservations':reservations})
  
def deleteR(request, reservation_id):
    id = int(reservation_id)  
    reservation = ReservationCreate.objects.get(id=id)
    if reservation is not None:
        reservation.delete()
    return redirect('liste')    

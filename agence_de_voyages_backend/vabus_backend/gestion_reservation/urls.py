from django.urls import path, include
from gestion_reservation.views import *
from gestion_reservation import views

# import routers from the REST framework
# it is necessary for routing
from rest_framework import routers
# create a router object
router = routers.DefaultRouter()
 
# register the router
router.register(r'reservation',views.reservationView, 'task')

urlpatterns = [
    # path('', homes, name="homes"),
    path('reservation/form',reserver_form, name='reserver_form'),
    path('reservations', liste , name='liste'),
    path('deleteR/<int:reservation_id>', deleteR, name='deleteR'),
    path('api/', include(router.urls)),
    
]

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
    path('', include(router.urls)),
    path('reservationList',views.ListReservationView.as_view(), name='reservation'),
    path('add_reservation/',views.CreateReservationView.as_view(), name='create_reservation'),
    path('<pk>/update_reservation/',views.UpdateReservationView.as_view(), name='reservation_update'),
    path('<pk>/delete_reservation/',views.DeleteReservationView.as_view(), name='reservation_delete'),    
    
]



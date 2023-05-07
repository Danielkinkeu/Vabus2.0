# import serializers from the REST framework
from rest_framework import serializers
 
# import the todo data model
from .models import ReservationCreate
 
# create a serializer class
class reservationSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = ReservationCreate
        fields = ('depart', 'destination','datedepart','qte','user','agence')
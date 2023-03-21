# import serializers from the REST framework
from rest_framework import serializers
 
# import the todo data model
from .models import Gestionagence
 
# create a serializer class
class adminSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Gestionagence
        fields = ('name', 'picture','siege','telephone','description', 'published')
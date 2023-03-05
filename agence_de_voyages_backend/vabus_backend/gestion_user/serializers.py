# import serializers from the REST framework
from rest_framework import serializers
 
# import the todo data model
from .models import UserRegisterform
 
# create a serializer class
class userSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = UserRegisterform
        fields = ('firstname', 'lastname','email','password1','password2')
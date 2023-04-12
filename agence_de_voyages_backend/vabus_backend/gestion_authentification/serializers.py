from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from .models import Account

# from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated
from .models import Account
UserModel = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password')
        
    password = serializers.CharField(min_length=8, write_only=True, validators=[validate_password])

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

   
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'password')
        
    email = serializers.EmailField()
    password = serializers.CharField(max_length=15, write_only=True)
        
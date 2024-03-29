# import view sets from the REST framework
from rest_framework import viewsets
# import the userSerializer from the serializer file
from .serializers import userSerializer
# import the user model from the models file
from .models import UserRegisterform
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# create a class for the user model viewsets
class userView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the userSerializer class
    serializer_class = userSerializer
 
    # define a variable and populate it
    # with the user objects
    queryset = UserRegisterform.objects.all()


class ListUserView(ListAPIView):
    queryset= UserRegisterform.objects.all()
    serializer_class= userSerializer

class CreateUserView(CreateAPIView):
    queryset= UserRegisterform.objects.all()
    serializer_class= userSerializer
    
class UpdateUserView(UpdateAPIView): 
    queryset= UserRegisterform.objects.all()
    serializer_class= userSerializer

class DeleteUserView(DestroyAPIView):
    queryset= UserRegisterform.objects.all()
    serializer_class= userSerializer
    
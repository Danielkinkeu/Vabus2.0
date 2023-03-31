# import view sets from the REST framework
from rest_framework import viewsets
# import the userSerializer from the serializer file
from .serializers import userSerializer
# import the user model from the models file
from .models import UserRegisterform

# create a class for the user model viewsets
class userView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the userSerializer class
    serializer_class = userSerializer
 
    # define a variable and populate it
    # with the user objects
    queryset = UserRegisterform.objects.all()

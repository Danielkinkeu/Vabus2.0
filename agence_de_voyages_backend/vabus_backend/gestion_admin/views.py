from .models import Gestionagence
# api 
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
# import view sets from the REST framework
from rest_framework import viewsets
# import the userSerializer from the serializer file
from .serializers import adminSerializer
from rest_framework.decorators import api_view
# import the user model from the models file
from .models import Gestionagence
from rest_framework.response import Response
# create a class for the user model viewsets

# class agenceView(APIView):
#     def get(self, request):
#         output = [{"name": output.name, "picture": output.picture, "siege": output.siege, "telephone": output.telephone, "description": output.description}
#                   for output in Gestionagence.objects.all()]
#         return Response(output)
#     def post(self, request):
#         serializer = adminSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
            
    
class adminView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the userSerializer class
    serializer_class = adminSerializer
 
    # define a variable and populate it
    # with the user objects
    queryset = Gestionagence.objects.all()
    
class ListAgenceView(ListAPIView):
    queryset= Gestionagence.objects.all()
    serializer_class= adminSerializer

class CreateAgenceView(CreateAPIView):
    queryset= Gestionagence.objects.all()
    serializer_class= adminSerializer
    
class UpdateAgenceView(UpdateAPIView): 
    queryset= Gestionagence.objects.all()
    serializer_class= adminSerializer

class DeleteAgenceView(DestroyAPIView):
    queryset= Gestionagence.objects.all()
    serializer_class= adminSerializer
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------
 
@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = Gestionagence.objects.all()

        serializer = adminSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = adminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def students_detail(request, name):
    try:
        student = Gestionagence.objects.get(pk=name)
    except Gestionagence.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = adminSerializer(student, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   
    
# -----------------------------------------------------------------------------------------------------------------------------------------------------


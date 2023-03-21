from django.shortcuts import render, redirect

from .models import Gestionagence
from .forms import GestionagenceCreate
from django.http import HttpResponse 
# api 

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

# import view sets from the REST framework
from rest_framework import viewsets
# import the userSerializer from the serializer file
from .serializers import adminSerializer
from rest_framework.decorators import api_view
# import the user model from the models file
from .models import Gestionagence
from rest_framework.response import Response
# create a class for the user model viewsets
class adminView(viewsets.ModelViewSet):
 
    # create a serializer class and
    # assign it to the userSerializer class
    serializer_class = adminSerializer
 
    # define a variable and populate it
    # with the user objects
    queryset = Gestionagence.objects.all()
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


def index(request):
      shelf = Gestionagence.objects.all()
      return render(request, 'library.html', {'shelf': shelf})
def upload(request):
    upload = GestionagenceCreate()
    if request.method == 'POST':
        upload = GestionagenceCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save() 
            return redirect('index')
        else:
            return HttpResponse(""" Something went wrong. Please reload the webpage by clicking <a href="{{url:'index'}}">Reload</a> """)
    else:
        return render (request, 'upload_form.html', {'upload_form': upload})
def update(request, gestionagence_id):
    gestionagence_id = int(gestionagence_id)
    try:
        crud_shelf = Gestionagence.objects.get(id = gestionagence_id)
    except Gestionagence.DoesNotExist:
        return redirect('index')
    crud_form = GestionagenceCreate(request.POST or None, instance = crud_shelf)
    if crud_form.is_valid():
        return redirect('index')  
    return render(request, 'upload_form.html', {'upload_form': crud_form})  
 
def delete(request, gestionagence_id):
    gestionagence_id = int(gestionagence_id)
    try:
        gestionagence_shelf = Gestionagence.objects.get(id = gestionagence_id)
    except Gestionagence.DoesNotExist:
        return redirect('index')
    gestionagence_shelf.delete()
    return redirect('index')         

# -----------------------------------------------------------------------------test--------------
# @api_view(['GET', 'POST', 'DELETE'])
# def tutorial_list(request):
#     if request.method == 'GET':
#         tutorials = Gestionagence.objects.all()
        
#         title = request.query_params.get('name', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
        
#         tutorials_serializer = adminSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#         # 'safe=False' for objects serialization
 
#     elif request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = adminSerializer(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         count = Gestionagence.objects.all().delete()
#         return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    


# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     try: 
#         tutorial = Gestionagence.objects.get(pk=pk) 
#     except Gestionagence.DoesNotExist: 
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
#     if request.method == 'GET': 
#         tutorial_serializer = adminSerializer(tutorial) 
#         return JsonResponse(tutorial_serializer.data) 
 
#     elif request.method == 'PUT': 
#         tutorial_data = JSONParser().parse(request) 
#         tutorial_serializer = adminSerializer(tutorial, data=tutorial_data) 
#         if tutorial_serializer.is_valid(): 
#             tutorial_serializer.save() 
#             return JsonResponse(tutorial_serializer.data) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
#     elif request.method == 'DELETE': 
#         tutorial.delete() 
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
       
# @api_view(['GET'])
# def tutorial_list_published(request):
#     tutorials = Gestionagence.objects.filter(published=True)
        
#     if request.method == 'GET': 
#         tutorials_serializer = adminSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)       
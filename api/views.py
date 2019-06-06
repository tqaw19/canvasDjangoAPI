from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

#Propios de la aplicación.
from rest_framework import viewsets
from .models import Curso
from .serializers import CursoSerializer
from django.shortcuts import render
import requests
import time
from rest_framework import status
from rest_framework.response import Response


class JSONResponse(HttpResponse):
    """
    An HttpResponse that rendes its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class CursoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Curso.objects.all().order_by('-id')
    serializer_class = CursoSerializer
    
#Estas variables globales serán utilizadas para todas las consultas.
#cd env/    $env: source bin/activate
#sudo service mysql start <----------------
#python manage.py runserver 0.0.0.0:8080 <-------------
BASE_URL = 'https://tecsup.instructure.com/api/v1'
#BASE_URL = 'http://3.88.106.84/api/v1'
headers = {'Authorization':'Bearer 8184~HbuKQy2rjk8SnjMmdQvdsh5e0WTCu7kXukmypkRFocQP4RwLDISO4gZDnMSCnrnM'} #teachkey
#headers = {'Authorization':'Bearer 8184~GyiG7Epa5z66YteeNG7pB1s8v0ObCWkydyC2RaUNXOXdkmyCWIjqy7fwnqWqQpS6'} #propio
#headers = {'Authorization':'Bearer 11maizMixV3gdpW9zChofr7wCqpaKSFLp26OPFYjRqsWNhkrCmFKKuBGuMIIMMen'} #canvasBitnami

def courses(request):
    if request.method == 'GET':
        url = "/courses"
        response = requests.get(BASE_URL + url, headers=headers)
        lista = response.json()
        return JSONResponse(lista)
        
def students(request, course_id):
    if request.method == 'GET':
        url = "/courses/" + course_id + "/students"
        response = requests.get(BASE_URL + url, headers=headers)
        lista = response.json()
        return JSONResponse(lista)
        
def enrollments(request, course_id):
    if request.method == 'GET':
        url = "/courses/" + course_id + "/enrollments"
        response = requests.get(BASE_URL + url, headers=headers)
        lista = response.json()
        return JSONResponse(lista)
        
def assignments(request, course_id):
    if request.method == 'GET':
        url = "/courses/" + course_id + "/assignments"
        response = requests.get(BASE_URL + url, headers=headers)
        lista = response.json()
        return JSONResponse(lista)
        
def users(request, user_id):
    if request.method == 'GET':
        url = "/users/" + user_id + "/enrollments"
        response = requests.get(BASE_URL + url, headers=headers)
        lista = response.json()
        return JSONResponse(lista)
        
#def enrollment_byid(request, account_id, id):
#    if request.method == 'GET':
#        url = "/accounts/" + account_id + "/enrollments/" + id
#        response = requests.get(BASE_URL + url, headers=headers)
#        lista = response.json()
#        return JSONResponse(lista)        
        
#App Agenda
def usuario_list(request):
    """
    List all code usuario, or create a new serie.
    """
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JSONResponse(serializer.data)
 
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    
def usuario_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        usuario = Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
         return HttpResponse(status=404)
 
    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return JSONResponse(serializer.data)
 
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
 
    elif request.method == 'DELETE':
        usuario.delete()
        return HttpResponse(status=204)

    
    
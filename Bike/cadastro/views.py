from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario
from .serializers import UsuaSerializer
from .forms import Form_Register_User
from django.contrib import messages
import json

def home(request):
    #template = loader.get_template('index.html')
    #context = {'image':"{%static 'images/Design sem nome (12) (1).png'%}"}
    #return HttpResponse(template.render(request))
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def form(request):
    form = Form_Register_User()
    return render(request, 'register_form.html', {'form':form})

@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request):
    if request.method == 'GET':
        try:
            if request.GET['user']:
                user_name = request.GET['user']
                try:
                    user = Usuario.objects.get(nome=user_name)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = UsuaSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'POST':
        nv_usuario = request.data
        serializer = UsuaSerializer(data=nv_usuario)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        nome = request.data['nome']
        try:
            updated_user = Usuario.objects.get(nome=nome)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UsuaSerializer(updated_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #DELETANDO DADOS
    elif request.method == 'DELETE':
        try:
            deleta_usua = Usuario.objects.get(nome=request.data['nome'])
            deleta_usua.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
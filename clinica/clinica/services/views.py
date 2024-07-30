from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import Group, User
from consultas.models import Paciente
from services.serializers import UserSerializer, GroupSerializer, PacienteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

@api_view(['GET'])
def saudacao(request):
    return Response({"saudacao": "Boa noite DEV I"})
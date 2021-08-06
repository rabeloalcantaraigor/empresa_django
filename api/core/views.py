from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Empresa, Funcionario
from .serializers import ClienteSerializer, EmpresaSerializer, FuncionarioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class=ClienteSerializer
    
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class=EmpresaSerializer
    
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class=FuncionarioSerializer

from django_filters.rest_framework import DjangoFilterBackend
#from django.shortcuts import render
from rest_framework.filters import SearchFilter
from core.serializers import ClienteSerializer, EmpresaSerializer, FuncionarioSerializer
from rest_framework import viewsets,permissions
from core.models import Cliente, Empresa, Funcionario

class ClienteViewSet(viewsets.ModelViewSet):
    #queryset = Cliente.objects.all()
    #serializer_class=ClienteSerializer
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['cpf']
    search_fields = ['cpf']
    
class EmpresaViewSet(viewsets.ModelViewSet):
    #queryset = Empresa.objects.all()
    #serializer_class=EmpresaSerializer
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['cnpj']
    search_fields = ['cnpj']
    
    
class FuncionarioViewSet(viewsets.ModelViewSet):
    #queryset = Funcionario.objects.all()
    #serializer_class=FuncionarioSerializer
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['rg']
    search_fields = ['rg']

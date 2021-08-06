from rest_framework import serializers
from .models import Cliente, Empresa, Funcionario

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 
                  'nome',
                  'sobrenome',
                  'idade',
                  'rg',
                  'cpf',
                  'telefone',
                  'endereco')
                  
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('id', 
                  'nome_da_empresa',
                  'endereco',
                  'cnpj',
                  'quantidade_de_clientes',
                  'segmento_da_empresa')
                  
class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('id', 
                  'nome_do_funcionario',
                  'sobrenome',
                  'cpf',
                  'rg',
                  'tempo_de_servico',
                  'remuneracao')

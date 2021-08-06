from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    idade = models.IntegerField()
    rg = models.IntegerField()
    cpf = models.IntegerField()
    telefone=models.IntegerField()
    endereco = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Empresa(models.Model):
    
    EMPRESA = (
        ('MV','Moda e Vestuário'),
        ('SB','Saúde e beleza'),
        ('E','Eletrônicos'),
        ('G','Games'),
        ('CMB','Cama, mesa e banho'),
        ('AE','Artigos esportivos'),
        ('EI','Equipamentos industriais')
        )
    
    nome_da_empresa = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    cnpj=models.IntegerField()
    quantidade_de_clientes = models.IntegerField()
    segmento_da_empresa = models.CharField(max_length=8,choices=EMPRESA)
    
    def __str__(self):
        return self.nome_da_empresa

class Funcionario(models.Model):
    nome_do_funcionario = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.IntegerField()
    rg = models.IntegerField()
    tempo_de_servico = models.IntegerField()
    remuneracao = models.IntegerField()   
    
    def __str__(self):
        return self.nome_do_funcionario     


#class Categoria(models.Model):

#    Nome_da_categoria = models.CharField(max_length=100)

#    def __str__(self):

#       return self.Nome_da_categoria

#    Ativada = models.BooleanField()

#    Obs_da_categoria = models.TextField()

#    Data_de_cadastro_da_categoria = models.DateField()

#class Cliente(models.Model):

#    Categoria_do_cliente = models.ForeignKey(Categoria, on_delete=models.CASCADE)

#    Cliente_ativo = models.BooleanField()

#    Nome_fantasia = models.CharField(max_length=100)

#    def __str__(self):

#       return self.Nome_fantasia

#    Nome_do_cliente = models.CharField(max_length=100)

#    Razao_social = models.CharField(max_length=100)

    #Logo_do_cliente = models.ImageField(upload_to=’upload/’)
#    Logo_do_cliente = models.ImageField(upload_to=’upload/’)

#    Site_do_cliente = models.URLField()

#    TIPOJURIDICODOCLIENTE = (

#           (“MEI”, “Microempreendedor Individual”),

#           (“PF”, “Pessoa Física”),

#           (“CS”, “Simples”),

#           )

#    Tipo_juridico_do_cliente = models.CharField(max_length=50, choices=TIPOJURIDICODOCLIENTE)

#    Cnpj = models.CharField(max_length=100)

#    Inscricao_estadual = models.CharField(max_length=50)

#    RESPOSTACONTRATO = (

#           (“SC”, “Sem contrato”),

#           (“EN”, “Contrato em negociação”),

#           (“CC”, “Possui contrato”),

#           )

#    Possui_contrato = models.CharField(max_length=30, choices=RESPOSTACONTRATO)

#    Contrato_anexado = models.FileField(upload_to=’upload/’)

#    Valor_total_do_contrato = models.FloatField()
    
#    Endereco = models.CharField(max_length=300)
#    CEP = models.CharField(max_length=100)

#    Cidade = models.CharField(max_length=60)

#    ESTADO = (

#           (“AC”, “Acre”),
#
#           (“AL”, “Alagoas”),
#
#           (“AP”, “Amapá”),

#           (“AM”, “Amazonas”),

#           (“BA”, “Bahia”),

#           (“CE”, “Ceará”),

#           (“DF”, “Distrito Federal”),

#           (“ES”, “Espírito Santo”),

#           (“GO”, “Goiás”),

#           (“MA”, “Maranhão”),

#           (“MT”, “Mato Grosso”),

#           (“MS”, “Mato Grosso do Sul”),

#           (“MG”, “Minas Gerais”),

#           (“PA”, “Pará”),

#           (“PB”, “Paraíba”),

#           (“PR”, “Paraná”),

#           (“PE”, “Pernambuco”),

#           (“PI”, “Piauí”),

#           (“RJ”, “Rio de Janeiro”),

#           (“RS”, “Rio Grande do Sul”),

#           (“RO”, “Rondônia”),

#           (“RR”, “Roraima”),

#           (“SC”, “Santa Catarina”),

#           (“SP”, “São Paulo”),

#           (“SE”, “Sergipe”),

#           (“TO”, “Tocantins”),

#           )

#    Estado = models.CharField(max_length=60, choices=ESTADO)

#    Telefone_1 = models.CharField(max_length=50)

#    Telefone_2 = models.CharField(max_length=50)

#    Celular_1 = models.CharField(max_length=50)

#    Email_do_cliente = models.EmailField()

#    Obs_do_cliente = models.TextField()

#    Data_de_cadastro_do_cliente = models.DateField()

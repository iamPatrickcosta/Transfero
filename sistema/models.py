from django.utils import timezone
from django.db import models

# Aqui vai ficar a classe modelo do usuário
# nome, sobrenome, cpf, telefone, email, foto, endereço.

class Usuário(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    enredeco = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='imagens/%Y/%m')

    def __str__(self):
        return f'{self.name}  {self.sobrenome}'
    
class Genero(models.Model):
    nome = models.CharField(max_length=50)
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self): 
        return f"{self.nome}"
    
class Filme(models.Model):   
    nome_do_filme = models.CharField(max_length=50)
    ano_de_lancamento = models.DateField ()
    estudio = models.CharField(max_length=50)
    # genero = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete= models.SET_NULL, null= True)
    sinopse = models.TextField()
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self): 
        def __str__(self): 
            return f"{self.nome}"    
    


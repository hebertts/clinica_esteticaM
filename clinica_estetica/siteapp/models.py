from django.db import models
from django.contrib.auth.models import AbstractUser

class Servico(models.Model):
    nome = models.CharField("Nome do serviço", max_length=100)
    descricao = models.TextField("Descrição")
    preco = models.DecimalField("Preço (R$)", max_digits=6, decimal_places=2)
    imagem = models.ImageField("Imagem ilustrativa", upload_to='servicos/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='profissionais/', blank=True, null=True)
    servicos = models.ManyToManyField(Servico, related_name='profissionais')

    def __str__(self):
        return self.nome

class Cliente(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.TextField(blank=True)
    idade = models.IntegerField(blank=True, null=True)

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()

    def __str__(self):
        return f'{self.cliente.username} - {self.servico.nome} em {self.data_hora}'

class CarrinhoItem(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.servico.preco * self.quantidade

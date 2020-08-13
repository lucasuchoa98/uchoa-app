from django.db import models


class Cliente(models.Model):
    nome =  models.CharField(max_length=200)
    cpf = models.CharField(max_length=14,primary_key=True)
    fone = models.CharField(max_length=14,null=False, blank=False)

    def __str__(self):
        return self.nome


class Area(models.Model):
    codigo = models.IntegerField()

    def __str__(self):
        return "{}".format(self.codigo)

class Cobrador(models.Model):
    nome =  models.CharField(max_length=200)
    cpf = models.CharField(max_length=14,primary_key=True)
    fone = models.CharField(max_length=14,null=False, blank=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    valor = models.FloatField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cobrador = models.ForeignKey(Cobrador, on_delete=models.CASCADE)

    

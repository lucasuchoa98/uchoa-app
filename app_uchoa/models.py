from django.db import models
from django.conf import settings

tipo_de_emprestimo = (
    ('di','Diário'),
    ('se','Semanal'),
    ('qu','Quinzenal'),
    ('me','Mensal')
)
class Cliente(models.Model):
    nome =  models.CharField(max_length=200)
    cpf = models.CharField(max_length=14,primary_key=True)
    codigo = models.CharField(max_length=8, unique=True)
    fone = models.CharField(max_length=14,null=True, blank=True)
    detalhe = models.CharField(max_length=150,null=True, blank=True)

    doc_file = models.FileField(upload_to=settings.MEDIA_ROOT, null=True, blank=True)

    def __str__(self):
        return self.nome


class Area(models.Model):
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=50)


    def __str__(self):
        return "{}".format(self.codigo)

class Cobrador(models.Model):
    nome =  models.CharField(max_length=200)
    cpf = models.CharField(max_length=14,primary_key=True)
    fone = models.CharField(max_length=14,null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cobrador = models.ForeignKey(Cobrador, on_delete=models.CASCADE)
    tipo_emprestimo = models.CharField(max_length=10, choices=tipo_de_emprestimo)
    atraso = models.BooleanField()

class Parcela(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    date = models.DateField()
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2)

class ValeRua(models.Model):
    vale_vale = models.DecimalField(max_digits=10, decimal_places=2)
    cobrador = models.ForeignKey(Cobrador, on_delete=models.CASCADE)



    

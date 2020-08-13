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
    fone = models.CharField(max_length=14,null=False, blank=False)

    doc_file = models.FileField(upload_to=settings.MEDIA_ROOT)

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
    valor_emprestimo = models.FloatField(default = 0.0)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cobrador = models.ForeignKey(Cobrador, on_delete=models.CASCADE)
    tipo_emprestimo = models.CharField(max_length=10, choices=tipo_de_emprestimo)

class Parcela(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)
    date = models.DateField()
    valor_parcela = models.FloatField(default = 0.0)




    

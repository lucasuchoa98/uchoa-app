from django.db import models
from django.conf import settings
from datetime import date
tipo_de_emprestimo = (
    ('di','Diário'),
    ('se','Semanal'),
    ('qu','Quinzenal'),
    ('me','Mensal')
)
class Area(models.Model):
    codigo = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=50, default='')


    def __str__(self):
        return "{}".format(self.codigo)



class Cliente(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    nome =  models.CharField(max_length=200,  blank=True, null=True)
    cpf = models.CharField(max_length=14,unique=True)
    codigo = models.CharField(max_length=8,unique=True,  null=True)
    fone = models.CharField(max_length=14,null=True, blank=True)
    detalhe = models.CharField(max_length=150,default='')
    doc_file = models.FileField(upload_to=settings.MEDIA_ROOT, null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['created']

class Cobrador(models.Model):
    nome =  models.CharField(max_length=200, default='')
    cpf = models.CharField(max_length=14,primary_key=True)
    fone = models.CharField(max_length=14,null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='emprestimos')
    tipo_emprestimo = models.CharField(max_length=10, choices=tipo_de_emprestimo, default='di')
    falta = models.BooleanField(default=False)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    date_start = models.DateField(default=date.today())

class Parcela(models.Model):
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE, related_name='parcelas')
    date = models.DateField(default=date.today())
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class ValeRua(models.Model):
    vale_vale = models.DecimalField(max_digits=10, decimal_places=2)
    cobrador = models.ForeignKey(Cobrador, on_delete=models.CASCADE)

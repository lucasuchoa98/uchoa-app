from .models import Cliente, Area, Cobrador, Emprestimo, Parcela, ValeRua
from rest_framework import routers, serializers, viewsets

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','created','nome','cpf','codigo','fone','detalhe','doc_file']

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['codigo','descricao']

class CobradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobrador
        fields = ['nome','fone']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['tipo_emprestimo','falta','cliente','valor_pago','cobrador','valor_emprestimo']

class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        fields = ['emprestimo','date','valor_parcela']

class ValeRuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValeRua
        fields = ['vale_vale','cobrador']
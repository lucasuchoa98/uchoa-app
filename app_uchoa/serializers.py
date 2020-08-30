from .models import Cliente, Area, Cobrador, Emprestimo, Parcela, ValeRua
from rest_framework import routers, serializers, viewsets

class ClienteSerializer(serializers.ModelSerializer):
    cliente = serializers.CharField(read_only=True)

    class Meta:
        model = Cliente
        fields = ['id','created','nome','cpf','codigo','fone','detalhe','doc_file','cliente']

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['codigo','descricao']

class CobradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobrador
        fields = ['nome','fone']

class EmprestimoSerializer(serializers.ModelSerializer):
    cliente_name = serializers.CharField(source= 'cliente.nome', read_only=True)
    class Meta:
        model = Emprestimo
        fields = ['pk','tipo_emprestimo','falta','cliente_name','valor_pago','valor_emprestimo']

class ParcelaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Parcela
        fields = ['date','valor_parcela']

class ValeRuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValeRua
        fields = ['vale_vale','cobrador']

from django import forms
from .models import Cliente, Cobrador, Emprestimo, ValeRua, Area, Parcela

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf','codigo','fone','detalhe','doc_file']

class CobradorForm(forms.ModelForm):
    class Meta:
        model = Cobrador
        fields = ['nome','fone']
    
class ValeRuaForm(forms.ModelForm):
    class Meta:
        model = ValeRua
        fields = ['vale_vale','cobrador']
    
class EmpretimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['tipo_emprestimo','falta','cliente','valor_pago','cobrador','valor_emprestimo']

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['codigo','descricao']

class ParcelaForm(forms.ModelForm):
    class Meta:
        model = Parcela
        fields = ['date','valor_parcela']
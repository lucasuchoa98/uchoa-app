from django.shortcuts import render, redirect
from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.reverse import reverse

from django.db import transaction
from django.http import JsonResponse

from .models import Area, Cliente, Cobrador, Emprestimo, Parcela, ValeRua

import time


@api_view(['GET', 'POST'])
def home(request):
    context = {}
    if request.user.is_authenticated:
        if request.method=='GET':
            area = Area.objects.all()
            serializer = AreaSerializer(area, many=True)
            context['areas'] = serializer.data
            return render(request, 'app_uchoa/home.html', context)

        elif request.method=='POST':
            pass
    else:
        return redirect(login)

@api_view(['GET', 'POST'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def cliente(request, *args, **kwargs):
    context = {}
    if request.method=="GET":
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        context['clientes'] = serializer.data
        print(**kwargs)
        #print(serializer.data)
        return Response(context, template_name='app_uchoa/cliente.html')
        #return render(request,  'app_uchoa/cliente.html', context)

@api_view(['GET', 'PUT', 'DELETE'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def clientedetail(request, id, *args, **kwargs):
    try:
        cli = Cliente.objects.get(id=id)
        context = {}
    except cli.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer = ClienteSerializer(cli)
        emp_query = Emprestimo.objects.filter(cliente=cli)
        serializer_emp = EmprestimoSerializer(emp_query, many=True)

        context['emprestimos'] = serializer_emp.data
        context['clientes'] = serializer.data

        print(serializer_emp.data)
        
        return Response(context, template_name='app_uchoa/cliente_detail.html')

    elif request.method == 'PUT':
        serializer = ClienteSerializer(cli, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(context, template_name='app_uchoa/cliente_detail.html')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cli.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def login(request):
    return HttpResponse('aqui sera a pagina de login')

def area(request,codigo):
    context = {}
    if request.method=="GET":
        area = Area.objects.get(codigo=codigo)
        cobrador = Cobrador.objects.filter(area=area)
        emprestimo = Emprestimo.objects.filter(cobrador=cobrador)

        area_serializer = AreaSerializer(area)
        cobrador_serializer = CobradorSerializer(cobrador)
        emprestimo_serializer = EmprestimoSerializer(emprestimo)


        context['area'] = area_serializer.data
        context['cobrador'] = cobrador_serializer.data
        context['emprestimo'] = emprestimo_serializer.data

        return render(request,  'app_uchoa/area.html', context)

def emprestimo(request):
    context = {}
    if request.method=="GET":
        emprestimos = Emprestimo.objects.all()
        serializer = EmprestimoSerializer(emprestimos, many=True)
        context['emprestimos'] = serializer.data
        print(serializer.data)
        return render(request,  'app_uchoa/emprestimos.html', context)

def emprestimodetail(request,id):
    context = {}
    if request.method=="GET":
        emprestimos = Emprestimo.objects.get(id=id)
        serializer = EmprestimoSerializer(emprestimos)
        context['emprestimos'] = serializer.data
        print(serializer.data)
        return render(request,  'app_uchoa/emprestimos.html', context)









class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CobradorViewSet(viewsets.ModelViewSet):
    queryset = Cobrador.objects.all()
    serializer_class = CobradorSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class ParcelaViewSet(viewsets.ModelViewSet):
    queryset = Parcela.objects.all()
    serializer_class = ParcelaSerializer

class ValeRuaViewSet(viewsets.ModelViewSet):
    queryset = ValeRua.objects.all()
    serializer_class = ValeRuaSerializer

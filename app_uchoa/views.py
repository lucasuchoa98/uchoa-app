from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from rest_framework import viewsets, status
from .serializers import *
from rest_framework.decorators import api_view, renderer_classes, permission_classes
<<<<<<< HEAD
=======
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
>>>>>>> d6cede91821b744683b77049db546de39aacce76
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ClienteForm, EmpretimoForm, ValeRuaForm, AreaForm, CobradorForm, ParcelaForm

from django.db import transaction
from django.http import JsonResponse

from .models import Area, Cliente, Cobrador, Emprestimo, Parcela, ValeRua, Profile

import time

@login_required
@api_view(['GET', 'POST'])
def home(request):
    context = {}
    if request.method=='GET':
        usuario = Profile.objects.get(user=request.user)
        role = usuario.role
        area = Area.objects.all()
        serializer = AreaSerializer(area, many=True)
        context['role'] = role
        context['areas'] = serializer.data
        return render(request, 'app_uchoa/home.html', context)

    elif request.method=='POST':
        pass

@login_required
@api_view(['GET', 'POST'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def cliente(request, *args, **kwargs):
    context = {}
    if request.method=="GET":
        form = ClienteForm()
        cli = Cliente.objects.all()
        paginator = Paginator(cli, 10)

        page = request.GET.get('page')
        try:
            clientes = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            clientes = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            clientes = paginator.page(paginator.num_pages)


        serializer = ClienteSerializer(cli, many=True)
        

        context['clientes'] = clientes

        context['form'] = form
        
    if request.method=='POST':
        form = ClienteForm(request.data)
        if form.is_valid():
            form.save()
            return redirect(cliente)

    return render(request,  'app_uchoa/cliente.html', context)

@login_required
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def clientedetail(request, id, *args, **kwargs):
    print('arg',*args)
    print('kwarg',**kwargs)
    try:
        cli = Cliente.objects.get(id=id)
        context = {}
    except cli.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer = ClienteSerializer(cli)
        emp_query = Emprestimo.objects.filter(cliente=cli)
        serializer_emp = EmprestimoSerializer(emp_query, many=True)
        form = EmpretimoForm()

        context['emprestimos'] = serializer_emp.data
        context['clientes'] = serializer.data
        context['form'] = form

        print('\n',serializer_emp.data)
        
        return Response(context, template_name='app_uchoa/cliente_detail.html')
    
    if request.method == 'POST':
        form = EmpretimoForm(request.data)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.cliente = Cliente.objects.get(id=id)
            emprestimo.valor_pago = 0.0
            emprestimo.falta = False
            emprestimo.save()
            return redirect(clientedetail, id)

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

@login_required
@api_view(['GET' ,'POST'])
def area(request,codigo):
    context = {}
    try:
        area = Area.objects.get(codigo=codigo)
    except:
        return redirect(home)
    if request.method=="GET":

        serializer = AreaSerializer(area)

        context['area'] = serializer.data

        return render(request, 'app_uchoa/area.html', context)

    if request.method=="POST":
        form = request.POST.get('codigo')
        context['codigo'] = form
        form = ClienteForm()
        cli = Cliente.objects.filter(area=area)
        serializer = ClienteSerializer(cli, many=True)

        context['clientes'] = serializer.data
        context['form'] = form
        return render(request, 'app_uchoa/cliente.html',context)
        
@login_required
def emprestimo(request):
    context = {}
    if request.method=="GET":
        emprestimos = Emprestimo.objects.all()
        serializer = EmprestimoSerializer(emprestimos, many=True)
        context['emprestimos'] = serializer.data
        print(serializer.data)
        return render(request,  'app_uchoa/emprestimos.html', context)

@login_required
@api_view(['GET', 'PUT', 'POST'])
def emprestimodetail(request,pk):
    try:
        emp = Emprestimo.objects.get(pk=pk)
        context = {}
    except:
        return Response(status=status.HTTP_404_NOT_FOUND, template_name='app_uchoa/emprestimo_detail.html')
    context = {}
    if request.method=="GET":
        serializer = EmprestimoSerializer(emp)
        parcelas = Parcela.objects.filter(emprestimo=emp)
        par_serializer = ParcelaSerializer(parcelas, many=True)
        form = ParcelaForm()


        context['emprestimos'] = serializer.data
        context['parcelas'] = par_serializer.data

        resto = float(serializer.data['valor_emprestimo']) - float(serializer.data['valor_pago']) 
        context['resto'] = resto
        context['form'] = form
        return render(request, 'app_uchoa/emprestimo_detail.html', context)
    
    if request.method=='POST':
        form = ParcelaForm(request.data)
        if form.is_valid:
            parcela = form.save(commit=False)
            parcela.emprestimo = Emprestimo.objects.get(pk=pk)
            form.save()
            return redirect(emprestimodetail, pk)

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    permission_classes = [IsAuthenticatedOrReadOnly]
=======
    permission_classes = [AllowAny]
>>>>>>> d6cede91821b744683b77049db546de39aacce76
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

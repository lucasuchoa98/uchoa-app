from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Area, Cliente, Cobrador, Emprestimo, Parcela


def home(request):
    context = {}
    if request.user.is_authenticated:
        if request.method=='GET':
            area = Area.objects.all()
            context['areas'] = area
            return render(request, 'app_uchoa/home.html', context)
        elif reques.method=='POST':
            pass
    else:
        return redirect(login)

def cliente(request):
    if request.method=="GET":
        return HttpResponse('<h1>aqui sera a pagina de cliente</h1>')
def login(request):
    return HttpResponse('aqui sera a pagina de login')

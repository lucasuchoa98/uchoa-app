from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'app_uchoa/home.html', context)

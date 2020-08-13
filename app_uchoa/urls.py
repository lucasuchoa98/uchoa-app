from django.contrib import admin
from django.urls import path

from .views import home,cliente,login

urlpatterns = [
    path('', home, name='home'),
    path('cliente/', cliente, name='cliente'),
    path('login/', login, name='login'),
]

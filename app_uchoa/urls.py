from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from .views import (home,
    cliente, 
    clientedetail, 
    emprestimodetail, 
    login, 
    area, 
    emprestimo,
    ClienteViewSet, 
    AreaViewSet, 
    CobradorViewSet, 
    EmprestimoViewSet, 
    ParcelaViewSet,
    ValeRuaViewSet
)


api_pathern = 'api/'


router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('areas', AreaViewSet)
router.register('cobradores', CobradorViewSet)
router.register('emprestimos', EmprestimoViewSet)
router.register('parcelas', ParcelaViewSet)
router.register('vales', ValeRuaViewSet)

urlpatterns = [
    path('', home, name='home'),
    path(api_pathern+'v1/', include(router.urls)),
    path('cliente/<int:id>/', clientedetail, name='clientedetail'),
    path('cliente/', cliente, name='cliente'),
    path('emprestimo/', emprestimo, name='emprestimo'),
    path('emprestimo/<int:pk>/', emprestimodetail, name='emprestimodetail'),
    path('login/', login, name='login'),
    path('area/<int:codigo>/', area, name='area'),

]

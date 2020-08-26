
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_uchoa.urls')),
    path('ap1/v1', include('rest_framework.urls')),
]

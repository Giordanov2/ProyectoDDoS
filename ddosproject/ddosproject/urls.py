"""
     Paths in our website like /login, /register and more
"""
from django.contrib import admin
from django.urls import path, include

from django.http import HttpRequest, HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('analisis.urls'))
]

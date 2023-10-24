"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appdopedro import views

urlpatterns = [
  path('', views.home, name = "home"), 
  path('dias',views.create_dia),
  path('dias/update/<id>',views.update_dia),
  path('dias/delete/<id>',views.delete_dia),
  path('num', views.create_numero),
  path('num/update/<id>', views.update_numero),
  path('num/delete/<id>', views.delete_numero),
  path('admin/', admin.site.urls),
]

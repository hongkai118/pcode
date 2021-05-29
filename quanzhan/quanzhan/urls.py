"""quanzhan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('classes/', views.classes),
    path('add_classes/', views.add_classes),
    path('del_classes/', views.del_classes),
    path('edit_classes/', views.edit_classes),
    path('teacher/', views.teacher),
    path('add_teacher/', views.add_teacher),
    path('del_teacher/', views.del_teacher),
    path('edit_teacher/', views.edit_teacher),
    path('student/', views.student)

]

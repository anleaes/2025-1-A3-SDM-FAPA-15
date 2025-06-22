"""
URL configuration for obraapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projecttype/', include('projecttype.urls', namespace='projecttype')),
    path('project/', include('project.urls', namespace='project')),
    path('stage/', include('stage.urls', namespace='stage')),
    path('employee/', include('employee.urls', namespace='employee')),
    path('employeestage/', include('employeestage.urls', namespace='employeestage')),
    path('supplier/', include('supplier.urls', namespace='supplier')),
    path('material/', include('material.urls', namespace='material')),





]

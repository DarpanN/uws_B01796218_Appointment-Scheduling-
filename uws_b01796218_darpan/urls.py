"""
URL configuration for uws_b01796218_darpan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.shortcuts import redirect
from . import views
from .views import client_list, employee_list, employee_service_list

urlpatterns = [
    # Redirect the root URL to the admin login page
    path('', lambda request: redirect('/admin/')),  # Redirects homepage to /admin/
    
    path('admin/', admin.site.urls),
    path('staff/', include('staff_accounts_SME.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('scheduling/', include('scheduling.urls')),
    


]






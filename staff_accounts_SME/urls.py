# project_name/urls.py
from django.contrib import admin
from django.urls import path, include  # include is important here

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('dashboard/', views.dashboard, name='dashboard'),

]
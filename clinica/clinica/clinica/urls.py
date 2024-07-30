from django.contrib import admin
from django.urls import path, include
from . import views as base

urlpatterns = [
    path('', base.index),
    path('admin/', admin.site.urls),
    path('consultas/', include('consultas.urls')),
    path('contas/', include('django.contrib.auth.urls')),
    path('services/', include('services.urls')),

]

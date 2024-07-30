from django.urls import path
from rest_framework import routers
from services import views

app_name = 'services'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'paciente', views.PacienteViewSet)

urlpatterns = [
    path('saudacao/', views.saudacao, name="saudacao"),
    path('paciente/', views.Paciente, name="paciente")
]

urlpatterns += router.urls

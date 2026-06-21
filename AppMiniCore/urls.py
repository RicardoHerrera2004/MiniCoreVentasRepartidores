from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.reporte_costos, name='reporte_costos'),
]
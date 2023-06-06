from django.urls import path
from . import views

urlpatterns = [
    path('risco_retorno/', views.histograma_retorno, name='histograma_retorno'),
]
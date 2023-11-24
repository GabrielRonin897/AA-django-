# urls.py

from django.urls import path
from .views import listar_produtos, processar_pedido

urlpatterns = [
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('processar_pedido/', processar_pedido, name='processar_pedido'),
]

